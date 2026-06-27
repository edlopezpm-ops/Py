from __future__ import annotations

import csv
import html
import io
import json
import mimetypes
import re
import sys
import textwrap
import traceback
import urllib.parse
import zipfile
from collections import Counter
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
CORE_DIR = ROOT / "core"
JOBS_DIR = ROOT / "jobs"
OUTPUT_DIR = ROOT / "output" / "pdf"
CORE_CV = CORE_DIR / "core-cv.txt"
CORE_EXPERIENCE = CORE_DIR / "core-experience.txt"
BASE_CV = DATA_DIR / "sample-cv.json"
HOST = "127.0.0.1"
PORT = 8765


STOPWORDS = {
    "a", "about", "above", "across", "after", "all", "also", "an", "and",
    "are", "as", "at", "be", "by", "can", "con", "de", "del", "desde",
    "el", "en", "for", "from", "have", "in", "is", "it", "la", "las",
    "los", "of", "on", "or", "para", "por", "que", "se", "sin", "sus",
    "the", "their", "this", "to", "un", "una", "with", "y", "you",
}

IMPORTANT_TERMS = {
    "python", "sql", "excel", "power bi", "tableau", "crm", "salesforce",
    "hubspot", "customer success", "customer support", "operations",
    "analyst", "data", "reporting", "dashboard", "automation", "api",
    "html", "css", "javascript", "bilingual", "spanish", "english",
    "process", "documentation", "workflow", "troubleshooting",
}


def ensure_dirs() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    CORE_DIR.mkdir(exist_ok=True)
    JOBS_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_base_cv() -> dict:
    if CORE_CV.exists():
        return core_to_cv(load_core_documents())
    with BASE_CV.open("r", encoding="utf-8") as source:
        return normalize_cv(json.load(source))


def read_text_preserve(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n")


def load_core_documents() -> dict:
    return {
        "cv": read_text_preserve(CORE_CV) if CORE_CV.exists() else "",
        "experience": read_text_preserve(CORE_EXPERIENCE) if CORE_EXPERIENCE.exists() else "",
        "cv_file": CORE_CV.name,
        "experience_file": CORE_EXPERIENCE.name,
    }


def split_skill_line(line: str) -> list[str]:
    normalized = line.replace("•", "|").replace("â€¢", "|")
    return [part.strip(" -") for part in normalized.split("|") if part.strip(" -")]


def lines_between(text: str, start_pattern: str, end_pattern: str | None = None) -> list[str]:
    lines = text.splitlines()
    start = 0
    end = len(lines)
    for index, line in enumerate(lines):
        if re.search(start_pattern, line, re.I):
            start = index + 1
            break
    if end_pattern:
        for index in range(start, len(lines)):
            if re.search(end_pattern, lines[index], re.I):
                end = index
                break
    return [line.strip() for line in lines[start:end] if line.strip()]


def core_to_cv(core: dict) -> dict:
    text = core.get("cv") or ""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    name = lines[0].strip("# ").title() if lines else "Candidate"
    contact_line = next((line for line in lines if "@" in line or re.search(r"\d{3}[-.]\d{3}", line)), "")
    email_match = re.search(r"[\w.+-]+@[\w.-]+\.\w+", contact_line)
    phone_match = re.search(r"(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}", contact_line)
    title = next((line.strip("# ") for line in lines if line.startswith("# ") and not line.upper().startswith("# PROFESSIONAL")), "Professional")
    summary_lines = lines_between(text, r"SUPPLY CHAIN|PROFESSIONAL SUMMARY", r"CORE EXPERTISE|PROFESSIONAL EXPERIENCE")
    summary = " ".join(line.strip("# ") for line in summary_lines[:4])
    if not summary:
        summary = "Enterprise technology and operations professional with leadership, consulting, support, and implementation experience."

    skills: list[str] = []
    for line in lines_between(text, r"CORE EXPERTISE", r"PROFESSIONAL EXPERIENCE"):
        if line.startswith("#") or set(line) <= {"-"}:
            continue
        for skill in split_skill_line(line):
            if 2 < len(skill) < 60 and skill.lower() not in {"supply chain & operations", "enterprise technology", "enterprise applications", "leadership & delivery"}:
                if skill not in skills:
                    skills.append(skill)

    experience: list[dict] = []
    current_company = ""
    current_role = ""
    current_period = ""
    current_bullets: list[str] = []
    for raw in lines_between(text, r"PROFESSIONAL EXPERIENCE", r"EARLY CAREER FOUNDATION|EDUCATION"):
        line = raw.strip()
        if line.startswith("## "):
            if current_company or current_bullets:
                experience.append({"role": current_role, "company": current_company, "period": current_period, "bullets": current_bullets})
            current_company = line.strip("# ").title()
            current_role = ""
            current_period = ""
            current_bullets = []
        elif "|" in line and not current_role:
            parts = [part.strip() for part in line.split("|")]
            current_role = " | ".join(parts[:-1]) if len(parts) > 1 else line
            current_period = parts[-1] if len(parts) > 1 else ""
        elif line.startswith(("*", "-", "•")):
            bullet = line.lstrip("*-• ").strip()
            if bullet:
                current_bullets.append(bullet)
    if current_company or current_bullets:
        experience.append({"role": current_role, "company": current_company, "period": current_period, "bullets": current_bullets})

    education_lines = [line for line in lines_between(text, r"EDUCATION", r"ADDITIONAL INFORMATION") if not line.startswith("#")]
    education = []
    for index in range(0, len(education_lines), 2):
        degree = education_lines[index]
        institution = education_lines[index + 1] if index + 1 < len(education_lines) else ""
        education.append({"degree": degree, "institution": institution, "period": ""})

    return normalize_cv({
        "profile": {
            "name": name,
            "title": title,
            "location": "Atlanta, GA" if "Atlanta" in contact_line else "",
            "phone": phone_match.group(0) if phone_match else "",
            "email": email_match.group(0) if email_match else "",
            "linkedin": "",
            "summary": summary,
        },
        "skills": skills[:42],
        "experience": experience,
        "education": education,
    })


def normalize_cv(source: dict) -> dict:
    profile = source.get("profile") or {}
    return {
        "profile": {
            "name": str(profile.get("name") or ""),
            "title": str(profile.get("title") or ""),
            "location": str(profile.get("location") or ""),
            "phone": str(profile.get("phone") or ""),
            "email": str(profile.get("email") or ""),
            "linkedin": str(profile.get("linkedin") or ""),
            "summary": str(profile.get("summary") or ""),
        },
        "skills": [str(item) for item in source.get("skills") or []],
        "experience": [
            {
                "role": str(item.get("role") or ""),
                "company": str(item.get("company") or ""),
                "period": str(item.get("period") or ""),
                "bullets": [str(line) for line in item.get("bullets") or []],
            }
            for item in source.get("experience") or []
        ],
        "education": [
            {
                "degree": str(item.get("degree") or ""),
                "institution": str(item.get("institution") or ""),
                "period": str(item.get("period") or ""),
            }
            for item in source.get("education") or []
        ],
    }


def clean_text(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<script[\s\S]*?</script>", " ", value, flags=re.I)
    value = re.sub(r"<style[\s\S]*?</style>", " ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def read_docx(path: Path) -> str:
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    parts: list[str] = []
    with zipfile.ZipFile(path) as docx:
        xml_bytes = docx.read("word/document.xml")
    root = ElementTree.fromstring(xml_bytes)
    for paragraph in root.findall(".//w:p", ns):
        texts = [node.text or "" for node in paragraph.findall(".//w:t", ns)]
        if texts:
            parts.append("".join(texts))
    return "\n".join(parts)


def read_csv_text(path: Path) -> str:
    rows: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.reader(source)
        for row in reader:
            rows.append(" ".join(cell for cell in row if cell))
    return "\n".join(rows)


def read_job_file(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return clean_text(read_docx(path))
    if suffix == ".csv":
        return clean_text(read_csv_text(path))
    if suffix in {".html", ".htm"}:
        return clean_text(path.read_text(encoding="utf-8", errors="ignore"))
    if suffix in {".txt", ".md"}:
        return clean_text(path.read_text(encoding="utf-8", errors="ignore"))
    if suffix == ".doc":
        raise ValueError("Los .doc antiguos no se leen sin Word. Guardalo como .docx o .txt.")
    raise ValueError(f"Formato no soportado: {suffix}")


def list_jobs() -> list[dict]:
    supported = {".txt", ".md", ".csv", ".html", ".htm", ".docx", ".doc"}
    jobs = []
    for path in sorted(JOBS_DIR.iterdir()):
        if path.is_file() and path.suffix.lower() in supported:
            jobs.append({
                "name": path.name,
                "size": path.stat().st_size,
                "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds"),
            })
    return jobs


def tokens(text: str) -> list[str]:
    return [
        item.lower()
        for item in re.findall(r"[A-Za-z][A-Za-z0-9+#./-]{1,}", text)
        if item.lower() not in STOPWORDS and len(item) > 2
    ]


def extract_keywords(job_text: str, limit: int = 28) -> list[str]:
    lowered = job_text.lower()
    phrases = [term for term in IMPORTANT_TERMS if term in lowered]
    counts = Counter(tokens(job_text))
    frequent = [word for word, _ in counts.most_common(80)]
    merged: list[str] = []
    for item in phrases + frequent:
        normalized = item.strip().lower()
        if normalized and normalized not in merged:
            merged.append(normalized)
    return merged[:limit]


def score_text(text: str, keywords: list[str]) -> int:
    lower = text.lower()
    return sum(2 if " " in key and key in lower else 1 for key in keywords if key in lower)


def reorder_by_keywords(items: list, key_func, keywords: list[str]) -> list:
    return sorted(
        items,
        key=lambda item: score_text(key_func(item), keywords),
        reverse=True,
    )


def infer_target_title(job_text: str, fallback: str) -> str:
    lines = [line.strip() for line in re.split(r"[\r\n]+", job_text) if line.strip()]
    for line in lines[:12]:
        if 4 <= len(line) <= 80 and not line.endswith("."):
            if re.search(r"(analyst|specialist|developer|engineer|manager|coordinator|associate|representative|consultant|support|operations|success)", line, re.I):
                return line
    return fallback


def build_summary(cv: dict, title: str, matched_skills: list[str], keywords: list[str]) -> str:
    profile = cv["profile"]
    skill_part = ", ".join(matched_skills[:5]) or ", ".join(cv["skills"][:4])
    keyword_part = ", ".join(keywords[:5])
    base = profile.get("summary") or "Professional with experience in operational support, communication, and structured problem solving."
    return (
        f"{base} Targeting {title} roles with emphasis on {skill_part}. "
        f"Aligned with job keywords such as {keyword_part}, while keeping experience and achievements grounded in the base CV."
    )


def adapt_cv(base_cv: dict, job_text: str) -> dict:
    cv = normalize_cv(base_cv)
    keywords = extract_keywords(job_text)
    matched_skills = [
        skill for skill in reorder_by_keywords(cv["skills"], lambda item: item, keywords)
        if score_text(skill, keywords) > 0
    ]
    remaining_skills = [skill for skill in cv["skills"] if skill not in matched_skills]
    title = infer_target_title(job_text, cv["profile"]["title"])
    cv["profile"]["title"] = title
    cv["profile"]["summary"] = build_summary(cv, title, matched_skills, keywords)
    cv["skills"] = matched_skills + remaining_skills
    cv["experience"] = reorder_by_keywords(
        cv["experience"],
        lambda item: " ".join([item["role"], item["company"], *item["bullets"]]),
        keywords,
    )
    for item in cv["experience"]:
        item["bullets"] = reorder_by_keywords(item["bullets"], lambda line: line, keywords)
    combined_cv_text = " ".join([
        cv["profile"]["summary"],
        " ".join(cv["skills"]),
        " ".join(
            " ".join([item["role"], item["company"], *item["bullets"]])
            for item in cv["experience"]
        ),
    ]).lower()
    cv["analysis"] = {
        "keywords": keywords,
        "matched_skills": matched_skills,
        "missing_keywords": [
            key for key in keywords
            if key not in combined_cv_text
        ][:12],
        "note": "No se inventan datos: se priorizan skills y logros existentes segun el cargo.",
    }
    return cv


def assess_fit(core: dict, job_text: str) -> dict:
    keywords = extract_keywords(job_text, limit=34)
    combined_core = clean_text((core.get("cv") or "") + " " + (core.get("experience") or "")).lower()
    matched = [key for key in keywords if key in combined_core]
    missing = [key for key in keywords if key not in combined_core]
    coverage = len(matched) / max(1, len(keywords))
    score = min(96, max(8, round(coverage * 100)))
    if score >= 72:
        recommendation = "Proceed"
        verdict = "Buena probabilidad relativa: el core tiene bastante overlap con el cargo."
    elif score >= 48:
        recommendation = "Review"
        verdict = "Probabilidad media: se puede aplicar, pero conviene ajustar el enfoque antes."
    else:
        recommendation = "Pause"
        verdict = "Probabilidad baja: hay gaps importantes contra las palabras clave del cargo."
    return {
        "score": score,
        "recommendation": recommendation,
        "verdict": verdict,
        "matched_keywords": matched[:18],
        "missing_keywords": missing[:14],
        "keywords": keywords,
        "question": "Quieres proceder y generar CV + cover letter para este cargo?",
    }


def build_cover_letter(cv: dict, core: dict, job_text: str, assessment: dict) -> dict:
    profile = cv["profile"]
    target = profile.get("title") or infer_target_title(job_text, "the role")
    company = infer_company(job_text)
    matched = assessment.get("matched_keywords") or []
    skill_line = ", ".join(matched[:6]) or ", ".join(cv.get("skills", [])[:5])
    experience_hint = first_relevant_experience_line(core.get("experience") or core.get("cv") or "", matched)
    body = [
        f"Dear Hiring Team,",
        (
            f"I am applying for the {target} opportunity"
            + (f" at {company}" if company else "")
            + ". My background combines enterprise supply chain technology, WMS/ERP ecosystems, program delivery, production support, and customer-facing consulting across North and Latin America."
        ),
        (
            f"The role appears to emphasize {skill_line}. Those areas align with my experience supporting complex warehouse, distribution, fulfillment, integration, reporting, and operational recovery environments."
        ),
        (
            f"In my recent work, I have led and supported enterprise software implementations, escalations, technical troubleshooting, governance reviews, and cross-functional execution with engineering, cloud operations, business stakeholders, and customer leadership. {experience_hint}"
        ),
        (
            "I would welcome the opportunity to discuss how my mix of functional supply chain depth, hands-on technical troubleshooting, and team leadership can help the organization execute reliably and improve operational outcomes."
        ),
        "Sincerely,",
        profile.get("name") or "Candidate",
    ]
    return {
        "profile": profile,
        "target_title": target,
        "company": company,
        "paragraphs": body,
    }


def infer_company(job_text: str) -> str:
    lines = [line.strip() for line in re.split(r"[\r\n]+", job_text) if line.strip()]
    for line in lines[:18]:
        match = re.search(r"\b(?:at|with|for)\s+([A-Z][A-Za-z0-9&.,' -]{2,50})", line)
        if match:
            return match.group(1).strip(" .")
    return ""


def first_relevant_experience_line(experience_text: str, keywords: list[str]) -> str:
    candidates = []
    for raw in experience_text.splitlines():
        line = raw.strip().lstrip("*-• ").strip()
        if 60 <= len(line) <= 260:
            candidates.append(line)
    if not candidates:
        return ""
    ranked = reorder_by_keywords(candidates, lambda item: item, keywords)
    return ranked[0] if ranked else ""


def build_ai_prompt(core: dict, job_text: str, assessment: dict) -> str:
    return textwrap.dedent(f"""
    Actua como career coach y resume writer. Usa SOLO la informacion del Core CV y Core Experience.

    Objetivo:
    1. Revisar si vale la pena aplicar al cargo.
    2. Explicar la probabilidad en lenguaje simple.
    3. Si recomiendas aplicar, proponer mejoras honestas para el CV y cover letter.
    4. No inventar empresas, fechas, titulos, certificaciones ni logros.

    Assessment local de la app:
    Score: {assessment.get("score")}%
    Recomendacion: {assessment.get("recommendation")}
    Matched keywords: {", ".join(assessment.get("matched_keywords", []))}
    Missing keywords: {", ".join(assessment.get("missing_keywords", []))}

    Cargo:
    {job_text}

    Core CV:
    {core.get("cv", "")}

    Core Experience:
    {core.get("experience", "")}
    """).strip()


def safe_filename(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._ -]+", "", value).strip().replace(" ", "-")
    return value[:80] or "cv"


def generate_pdf(cv: dict) -> Path:
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import inch
        from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    except ImportError as exc:
        raise RuntimeError(
            "Falta reportlab. Instala con: py -m pip install reportlab"
        ) from exc

    profile = cv["profile"]
    filename = f"{safe_filename(profile.get('name'))}-{safe_filename(profile.get('title'))}.pdf"
    output = OUTPUT_DIR / filename
    styles = getSampleStyleSheet()
    body = ParagraphStyle("BodyCV", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=13)
    small = ParagraphStyle("SmallCV", parent=body, fontSize=8.5, textColor=colors.HexColor("#5f6b7a"))
    h1 = ParagraphStyle("Name", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=22, leading=26, spaceAfter=2)
    h2 = ParagraphStyle("Title", parent=body, fontName="Helvetica-Bold", fontSize=11, textColor=colors.HexColor("#0f766e"))
    section = ParagraphStyle("Section", parent=body, fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=colors.HexColor("#0f766e"), spaceBefore=11, spaceAfter=5)
    bullet_style = ParagraphStyle("Bullet", parent=body, leftIndent=12, firstLineIndent=-7, spaceAfter=3)
    doc = SimpleDocTemplate(
        str(output),
        pagesize=letter,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.50 * inch,
        bottomMargin=0.50 * inch,
    )

    def p(text: str, style=body) -> Paragraph:
        return Paragraph(html.escape(text or ""), style)

    story = [
        p(profile["name"], h1),
        p(profile["title"], h2),
        p(" | ".join(filter(None, [profile["location"], profile["phone"], profile["email"], profile["linkedin"]])), small),
        Spacer(1, 8),
        p("PROFESSIONAL SUMMARY", section),
        p(profile["summary"]),
        p("CORE SKILLS", section),
    ]
    skill_rows = []
    skills = cv.get("skills") or []
    for index in range(0, len(skills), 3):
        row = [p(item, small) for item in skills[index:index + 3]]
        while len(row) < 3:
            row.append(p("", small))
        skill_rows.append(row)
    if skill_rows:
        table = Table(skill_rows, colWidths=[2.35 * inch, 2.35 * inch, 2.35 * inch])
        table.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.25, colors.HexColor("#cfd7df")),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#cfd7df")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        story.append(table)

    story.append(p("EXPERIENCE", section))
    for item in cv.get("experience") or []:
        story.append(p(f"{item['role']} - {item['company']} ({item['period']})", h2))
        for bullet in item.get("bullets") or []:
            story.append(p(f"- {bullet}", bullet_style))

    story.append(p("EDUCATION", section))
    for item in cv.get("education") or []:
        story.append(p(f"{item['degree']} - {item['institution']} ({item['period']})", body))

    doc.build(story)
    return output


def generate_cover_letter_pdf(cover: dict) -> Path:
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import inch
        from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
    except ImportError as exc:
        raise RuntimeError(
            "Falta reportlab. Instala con: py -m pip install reportlab"
        ) from exc

    profile = cover.get("profile") or {}
    filename = f"{safe_filename(profile.get('name'))}-{safe_filename(cover.get('target_title'))}-cover-letter.pdf"
    output = OUTPUT_DIR / filename
    styles = getSampleStyleSheet()
    body = ParagraphStyle("LetterBody", parent=styles["BodyText"], fontName="Helvetica", fontSize=10.5, leading=15, spaceAfter=10)
    small = ParagraphStyle("LetterSmall", parent=body, fontSize=9, textColor=colors.HexColor("#5f6b7a"), spaceAfter=16)
    h1 = ParagraphStyle("LetterName", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=19, leading=23, spaceAfter=2)
    h2 = ParagraphStyle("LetterTitle", parent=body, fontName="Helvetica-Bold", fontSize=11, textColor=colors.HexColor("#0f766e"), spaceAfter=20)
    doc = SimpleDocTemplate(
        str(output),
        pagesize=letter,
        rightMargin=0.70 * inch,
        leftMargin=0.70 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
    )

    def p(text: str, style=body) -> Paragraph:
        return Paragraph(html.escape(text or ""), style)

    contact = " | ".join(filter(None, [profile.get("location"), profile.get("phone"), profile.get("email"), profile.get("linkedin")]))
    story = [
        p(profile.get("name") or "Candidate", h1),
        p(contact, small),
        p(f"Cover Letter - {cover.get('target_title') or 'Target Role'}", h2),
    ]
    for paragraph in cover.get("paragraphs") or []:
        story.append(p(paragraph, body))
        story.append(Spacer(1, 2))
    doc.build(story)
    return output


def build_application_package(job_text: str) -> dict:
    core = load_core_documents()
    base_cv = core_to_cv(core)
    assessment = assess_fit(core, job_text)
    cv = adapt_cv(base_cv, job_text)
    cv["analysis"].update({
        "fit_score": assessment["score"],
        "recommendation": assessment["recommendation"],
        "assessment_verdict": assessment["verdict"],
    })
    cover = build_cover_letter(cv, core, job_text, assessment)
    cv_path = generate_pdf(cv)
    cover_path = generate_cover_letter_pdf(cover)
    return {
        "cv": cv,
        "assessment": assessment,
        "cover_letter": cover,
        "files": [
            {"kind": "cv", "file": cv_path.name, "download_url": f"/download/{urllib.parse.quote(cv_path.name)}"},
            {"kind": "cover_letter", "file": cover_path.name, "download_url": f"/download/{urllib.parse.quote(cover_path.name)}"},
        ],
        "ai_prompt": build_ai_prompt(core, job_text, assessment),
    }


def json_response(handler: BaseHTTPRequestHandler, payload: dict, status: int = 200) -> None:
    body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def read_request_json(handler: BaseHTTPRequestHandler) -> dict:
    length = int(handler.headers.get("Content-Length") or "0")
    raw = handler.rfile.read(length).decode("utf-8")
    return json.loads(raw or "{}")


INDEX_HTML = r"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CV Local Generator Python</title>
  <style>
    :root {
      --bg: #f5f7f9;
      --panel: #fff;
      --ink: #17202a;
      --muted: #657384;
      --line: #d7dee7;
      --accent: #0f766e;
      --accent-dark: #0a5f59;
      --warn: #9a3412;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.45;
    }
    button, textarea, select, input { font: inherit; }
    .shell {
      min-height: 100vh;
      display: grid;
      grid-template-columns: minmax(330px, 430px) 1fr;
    }
    aside {
      background: var(--panel);
      border-right: 1px solid var(--line);
      padding: 18px;
      overflow: auto;
      max-height: 100vh;
    }
    main { padding: 24px; overflow: auto; max-height: 100vh; }
    h1 { margin: 0 0 14px; font-size: 22px; letter-spacing: 0; }
    h2 {
      margin: 18px 0 8px;
      font-size: 13px;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0;
    }
    label { display: block; margin: 12px 0 6px; font-weight: 700; font-size: 13px; }
    select, textarea, input {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 9px 10px;
      background: #fff;
      color: var(--ink);
    }
    textarea { min-height: 180px; resize: vertical; }
    .actions { display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0; }
    .btn {
      min-height: 38px;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      border-radius: 6px;
      padding: 8px 10px;
      cursor: pointer;
    }
    .btn:hover { border-color: var(--accent); }
    .btn.primary { color: #fff; background: var(--accent); border-color: var(--accent); }
    .btn.primary:hover { background: var(--accent-dark); }
    .hint { color: var(--muted); font-size: 13px; margin: 8px 0; }
    .status { color: var(--warn); font-size: 13px; min-height: 19px; }
    .preview {
      width: min(100%, 850px);
      margin: 0 auto;
      background: #fff;
      box-shadow: 0 18px 45px rgba(15, 23, 42, 0.12);
      padding: 52px 62px;
      min-height: 1040px;
    }
    .cv-header { border-bottom: 3px solid var(--accent); padding-bottom: 14px; margin-bottom: 20px; }
    .cv-name { margin: 0 0 4px; font-size: 32px; line-height: 1.1; letter-spacing: 0; }
    .cv-title { margin: 0; color: var(--accent); font-weight: 700; }
    .contact { margin-top: 10px; color: var(--muted); font-size: 13px; }
    .section { margin-top: 21px; }
    .section h3 {
      margin: 0 0 9px;
      color: var(--accent);
      border-bottom: 1px solid var(--line);
      padding-bottom: 5px;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 0;
    }
    .skills { display: flex; flex-wrap: wrap; gap: 7px; margin: 0; padding: 0; list-style: none; }
    .skills li { border: 1px solid var(--line); border-radius: 999px; padding: 5px 9px; font-size: 13px; }
    .entry { margin-bottom: 15px; }
    .entry-head { display: flex; justify-content: space-between; gap: 12px; align-items: baseline; }
    .entry-meta, .company { color: var(--muted); font-size: 13px; }
    .company { margin: 2px 0 6px; }
    .entry ul { margin: 6px 0 0 18px; padding: 0; }
    .chips { display: flex; flex-wrap: wrap; gap: 6px; }
    .chip { border: 1px solid var(--line); background: #f8fafc; border-radius: 999px; padding: 4px 8px; font-size: 12px; }
    .score-box {
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      background: #f8fafc;
      margin-top: 10px;
    }
    .score {
      font-size: 30px;
      font-weight: 700;
      color: var(--accent);
      line-height: 1;
    }
    .letter-preview p { margin: 0 0 12px; }
    @media (max-width: 900px) {
      .shell { grid-template-columns: 1fr; }
      aside, main { max-height: none; }
      aside { border-right: 0; border-bottom: 1px solid var(--line); }
      .preview { padding: 34px 24px; min-height: auto; }
      .entry-head { display: block; }
    }
  </style>
</head>
<body>
  <div class="shell">
    <aside>
      <h1>CV Local Generator</h1>
      <p class="hint">Usa <strong>core/core-cv.txt</strong> y <strong>core/core-experience.txt</strong> como masters. Para cambiar tu experiencia base, reemplaza esos archivos y refresca la app.</p>
      <div class="score-box">
        <strong>Masters activos</strong>
        <p class="hint" id="coreInfo">Leyendo archivos core...</p>
      </div>
      <label for="jobSelect">Cargo desde folder</label>
      <select id="jobSelect"></select>
      <div class="actions">
        <button class="btn" id="loadJobBtn" type="button">Cargar cargo</button>
        <button class="btn" id="refreshJobsBtn" type="button">Refrescar</button>
      </div>
      <label for="jobText">Descripcion del cargo</label>
      <textarea id="jobText" placeholder="Pega aqui el job posting o carga un archivo de jobs/"></textarea>
      <div class="actions">
        <button class="btn primary" id="adaptBtn" type="button">Evaluar cargo</button>
        <button class="btn" id="packageBtn" type="button" disabled>Generar CV + Cover Letter</button>
      </div>
      <p class="status" id="status"></p>
      <h2>Assessment</h2>
      <div class="score-box" id="assessmentBox">
        <div class="score" id="score">--%</div>
        <p class="hint" id="verdict">Carga un cargo para calcular probabilidad.</p>
        <p class="hint" id="question"></p>
      </div>
      <h2>Keywords detectadas</h2>
      <div class="chips" id="keywords"></div>
      <h2>Keywords faltantes</h2>
      <div class="chips" id="missing"></div>
      <h2>Prompt ChatGPT Free</h2>
      <textarea id="promptBox" spellcheck="false" placeholder="Aqui aparecera un prompt para copiar manualmente en ChatGPT si quieres una segunda revision sin API."></textarea>
      <h2>JSON editable</h2>
      <textarea id="jsonBox" spellcheck="false"></textarea>
    </aside>
    <main>
      <article class="preview" id="preview"></article>
      <article class="preview letter-preview" id="letterPreview" style="margin-top:24px;"></article>
    </main>
  </div>
  <script>
    const state = { cv: null, assessment: null, coverLetter: null };
    const $ = (id) => document.getElementById(id);
    const escapeHtml = (value) => String(value ?? "")
      .replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;").replaceAll("'", "&#039;");

    async function api(path, options = {}) {
      const response = await fetch(path, options);
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || "Error inesperado");
      return data;
    }

    function setStatus(message) { $("status").textContent = message || ""; }

    function chips(id, items) {
      $(id).innerHTML = (items || []).map(item => `<span class="chip">${escapeHtml(item)}</span>`).join("");
    }

    function renderAssessment(assessment) {
      state.assessment = assessment;
      $("score").textContent = assessment ? `${assessment.score}%` : "--%";
      $("verdict").textContent = assessment?.verdict || "Carga un cargo para calcular probabilidad.";
      $("question").textContent = assessment?.question || "";
      chips("keywords", assessment?.keywords || []);
      chips("missing", assessment?.missing_keywords || []);
      $("packageBtn").disabled = !assessment;
    }

    function renderCoverLetter(coverLetter) {
      state.coverLetter = coverLetter;
      if (!coverLetter) {
        $("letterPreview").innerHTML = "";
        return;
      }
      $("letterPreview").innerHTML = `
        <header class="cv-header">
          <h2 class="cv-name">${escapeHtml(coverLetter.profile?.name || "Candidate")}</h2>
          <p class="cv-title">Cover Letter - ${escapeHtml(coverLetter.target_title || "Target Role")}</p>
        </header>
        ${(coverLetter.paragraphs || []).map(paragraph => `<p>${escapeHtml(paragraph)}</p>`).join("")}
      `;
    }

    function render(cv) {
      state.cv = cv;
      $("jsonBox").value = JSON.stringify(cv, null, 2);
      const p = cv.profile;
      const contact = [p.location, p.phone, p.email, p.linkedin].filter(Boolean).join(" | ");
      const skills = (cv.skills || []).map(skill => `<li>${escapeHtml(skill)}</li>`).join("");
      const exp = (cv.experience || []).map(item => `
        <div class="entry">
          <div class="entry-head"><strong>${escapeHtml(item.role)}</strong><span class="entry-meta">${escapeHtml(item.period)}</span></div>
          <p class="company">${escapeHtml(item.company)}</p>
          <ul>${(item.bullets || []).map(line => `<li>${escapeHtml(line)}</li>`).join("")}</ul>
        </div>
      `).join("");
      const edu = (cv.education || []).map(item => `
        <div class="entry">
          <div class="entry-head"><strong>${escapeHtml(item.degree)}</strong><span class="entry-meta">${escapeHtml(item.period)}</span></div>
          <p class="company">${escapeHtml(item.institution)}</p>
        </div>
      `).join("");
      $("preview").innerHTML = `
        <header class="cv-header">
          <h2 class="cv-name">${escapeHtml(p.name)}</h2>
          <p class="cv-title">${escapeHtml(p.title)}</p>
          <div class="contact">${escapeHtml(contact)}</div>
        </header>
        <section class="section"><h3>Professional Summary</h3><p>${escapeHtml(p.summary)}</p></section>
        <section class="section"><h3>Core Skills</h3><ul class="skills">${skills}</ul></section>
        <section class="section"><h3>Experience</h3>${exp}</section>
        <section class="section"><h3>Education</h3>${edu}</section>
      `;
      if (!state.assessment) {
        chips("keywords", cv.analysis?.keywords || []);
        chips("missing", cv.analysis?.missing_keywords || []);
      }
    }

    async function loadJobs() {
      const data = await api("/api/jobs");
      $("jobSelect").innerHTML = data.jobs.map(job => `<option value="${escapeHtml(job.name)}">${escapeHtml(job.name)}</option>`).join("");
    }

    async function loadBase() {
      const data = await api("/api/cv");
      render(data.cv);
    }

    async function loadCoreInfo() {
      const data = await api("/api/core");
      const core = data.core;
      $("coreInfo").textContent = `${core.cv_file} (${core.cv_chars} chars) + ${core.experience_file} (${core.experience_chars} chars)`;
    }

    $("refreshJobsBtn").addEventListener("click", () => loadJobs().catch(err => setStatus(err.message)));
    $("loadJobBtn").addEventListener("click", async () => {
      try {
        const name = $("jobSelect").value;
        const data = await api(`/api/job?name=${encodeURIComponent(name)}`);
        $("jobText").value = data.text;
        setStatus(`Cargo cargado: ${name}`);
      } catch (err) { setStatus(err.message); }
    });
    $("adaptBtn").addEventListener("click", async () => {
      try {
        const data = await api("/api/adapt", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ job_text: $("jobText").value })
        });
        render(data.cv);
        renderAssessment(data.assessment);
        renderCoverLetter(data.cover_letter);
        $("promptBox").value = data.ai_prompt || "";
        setStatus("Assessment listo. Si decides proceder, genera CV + cover letter.");
      } catch (err) { setStatus(err.message); }
    });
    $("packageBtn").addEventListener("click", async () => {
      try {
        const data = await api("/api/package", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ job_text: $("jobText").value })
        });
        render(data.cv);
        renderAssessment(data.assessment);
        renderCoverLetter(data.cover_letter);
        $("promptBox").value = data.ai_prompt || "";
        setStatus(`Generados: ${data.files.map(file => file.file).join(" + ")}`);
        data.files.forEach(file => window.open(file.download_url, "_blank"));
      } catch (err) { setStatus(err.message); }
    });
    $("jsonBox").addEventListener("change", () => {
      try { render(JSON.parse($("jsonBox").value)); setStatus("JSON aplicado."); }
      catch (err) { setStatus("JSON invalido."); }
    });

    Promise.all([loadJobs(), loadBase(), loadCoreInfo()]).catch(err => setStatus(err.message));
  </script>
</body>
</html>
"""


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        try:
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path == "/":
                body = INDEX_HTML.encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            if parsed.path == "/api/jobs":
                json_response(self, {"jobs": list_jobs()})
                return
            if parsed.path == "/api/cv":
                cv = load_base_cv()
                cv["analysis"] = {"keywords": [], "matched_skills": [], "missing_keywords": [], "note": ""}
                json_response(self, {"cv": cv})
                return
            if parsed.path == "/api/core":
                core = load_core_documents()
                json_response(self, {
                    "core": {
                        "cv_file": core["cv_file"],
                        "experience_file": core["experience_file"],
                        "cv_chars": len(core["cv"]),
                        "experience_chars": len(core["experience"]),
                    }
                })
                return
            if parsed.path == "/api/job":
                params = urllib.parse.parse_qs(parsed.query)
                name = Path(params.get("name", [""])[0]).name
                path = JOBS_DIR / name
                if not path.exists():
                    json_response(self, {"error": "No encontre ese archivo en jobs/."}, 404)
                    return
                json_response(self, {"name": name, "text": read_job_file(path)})
                return
            if parsed.path.startswith("/download/"):
                name = Path(urllib.parse.unquote(parsed.path.removeprefix("/download/"))).name
                path = OUTPUT_DIR / name
                if not path.exists():
                    self.send_error(404)
                    return
                body = path.read_bytes()
                mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
                self.send_response(200)
                self.send_header("Content-Type", mime)
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Content-Disposition", f'inline; filename="{path.name}"')
                self.end_headers()
                self.wfile.write(body)
                return
            self.send_error(404)
        except Exception as exc:
            traceback.print_exc()
            json_response(self, {"error": str(exc)}, 500)

    def do_POST(self) -> None:
        try:
            if self.path == "/api/adapt":
                payload = read_request_json(self)
                job_text = clean_text(payload.get("job_text") or "")
                if not job_text:
                    json_response(self, {"error": "Pega o carga una descripcion del cargo primero."}, 400)
                    return
                core = load_core_documents()
                assessment = assess_fit(core, job_text)
                cv = adapt_cv(core_to_cv(core), job_text)
                cv["analysis"].update({
                    "fit_score": assessment["score"],
                    "recommendation": assessment["recommendation"],
                    "assessment_verdict": assessment["verdict"],
                })
                cover = build_cover_letter(cv, core, job_text, assessment)
                json_response(self, {
                    "cv": cv,
                    "assessment": assessment,
                    "cover_letter": cover,
                    "ai_prompt": build_ai_prompt(core, job_text, assessment),
                })
                return
            if self.path == "/api/package":
                payload = read_request_json(self)
                job_text = clean_text(payload.get("job_text") or "")
                if not job_text:
                    json_response(self, {"error": "Pega o carga una descripcion del cargo primero."}, 400)
                    return
                json_response(self, build_application_package(job_text))
                return
            if self.path == "/api/pdf":
                payload = read_request_json(self)
                cv = normalize_cv(payload.get("cv") or {})
                path = generate_pdf(cv)
                json_response(self, {
                    "file": path.name,
                    "download_url": f"/download/{urllib.parse.quote(path.name)}",
                })
                return
            self.send_error(404)
        except Exception as exc:
            traceback.print_exc()
            json_response(self, {"error": str(exc)}, 500)

    def log_message(self, format: str, *args) -> None:
        sys.stdout.write("%s - %s\n" % (self.address_string(), format % args))


def main() -> int:
    ensure_dirs()
    server = ThreadingHTTPServer((HOST, PORT), AppHandler)
    print(textwrap.dedent(f"""
    CV Local Generator listo.
    Abre: http://{HOST}:{PORT}
    Cargos soportados en jobs/: .txt, .md, .csv, .html, .htm, .docx
    Presiona Ctrl+C para cerrar.
    """).strip())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor cerrado.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
