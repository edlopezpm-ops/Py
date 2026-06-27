from __future__ import annotations

import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

import cv_app


class CVDesktopApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("CV Local Generator")
        self.geometry("1080x760")
        self.minsize(920, 650)
        self.assessment: dict | None = None
        self.package: dict | None = None
        self.ai_prompt = ""

        cv_app.ensure_dirs()
        self._configure_style()
        self._build_layout()
        self._load_core_info()
        self._load_job_list()

    def _configure_style(self) -> None:
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("TButton", padding=(10, 7))
        self.style.configure("Primary.TButton", padding=(12, 8))
        self.style.configure("Step.TLabel", font=("Segoe UI", 10, "bold"))
        self.style.configure("Title.TLabel", font=("Segoe UI", 18, "bold"))
        self.style.configure("Score.TLabel", font=("Segoe UI", 34, "bold"), foreground="#0f766e")

    def _build_layout(self) -> None:
        shell = ttk.Frame(self, padding=16)
        shell.pack(fill="both", expand=True)
        shell.columnconfigure(0, weight=2)
        shell.columnconfigure(1, weight=3)
        shell.rowconfigure(1, weight=1)

        header = ttk.Frame(shell)
        header.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 12))
        header.columnconfigure(0, weight=1)
        ttk.Label(header, text="CV Local Generator", style="Title.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Button(header, text="Abrir carpeta output", command=self._open_output_folder).grid(row=0, column=1, sticky="e")

        left = ttk.Frame(shell)
        left.grid(row=1, column=0, sticky="nsew", padx=(0, 12))
        left.columnconfigure(0, weight=1)
        left.rowconfigure(8, weight=1)

        right = ttk.Frame(shell)
        right.grid(row=1, column=1, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(1, weight=2)
        right.rowconfigure(3, weight=1)

        ttk.Label(left, text="Paso 1 - Confirma tus masters", style="Step.TLabel").grid(row=0, column=0, sticky="w")
        self.core_label = ttk.Label(left, text="Leyendo core...", wraplength=390)
        self.core_label.grid(row=1, column=0, sticky="ew", pady=(4, 12))

        ttk.Label(left, text="Paso 2 - Carga o pega el cargo", style="Step.TLabel").grid(row=2, column=0, sticky="w")
        job_row = ttk.Frame(left)
        job_row.grid(row=3, column=0, sticky="ew", pady=(6, 6))
        job_row.columnconfigure(0, weight=1)
        self.job_combo = ttk.Combobox(job_row, state="readonly")
        self.job_combo.grid(row=0, column=0, sticky="ew", padx=(0, 6))
        ttk.Button(job_row, text="Cargar", command=self._load_selected_job).grid(row=0, column=1)
        ttk.Button(job_row, text="Archivo...", command=self._browse_job_file).grid(row=0, column=2, padx=(6, 0))

        self.job_text = tk.Text(left, height=12, wrap="word", undo=True)
        self.job_text.grid(row=4, column=0, sticky="nsew", pady=(0, 12))

        ttk.Label(left, text="Paso 3 - Evalua el cargo", style="Step.TLabel").grid(row=5, column=0, sticky="w")
        action_row = ttk.Frame(left)
        action_row.grid(row=6, column=0, sticky="ew", pady=(6, 12))
        ttk.Button(action_row, text="Evaluar cargo", style="Primary.TButton", command=self._evaluate_job).pack(side="left")
        self.generate_button = ttk.Button(action_row, text="Generar CV + Cover Letter", command=self._generate_package, state="disabled")
        self.generate_button.pack(side="left", padx=(8, 0))

        self.status_var = tk.StringVar(value="Listo.")
        ttk.Label(left, textvariable=self.status_var, wraplength=390).grid(row=7, column=0, sticky="ew")

        ttk.Label(right, text="Assessment", style="Step.TLabel").grid(row=0, column=0, sticky="w")
        assessment_frame = ttk.Frame(right, padding=12, relief="solid")
        assessment_frame.grid(row=1, column=0, sticky="nsew", pady=(6, 12))
        assessment_frame.columnconfigure(1, weight=1)
        self.score_label = ttk.Label(assessment_frame, text="--%", style="Score.TLabel")
        self.score_label.grid(row=0, column=0, rowspan=2, sticky="nw", padx=(0, 16))
        self.verdict_text = tk.Text(assessment_frame, height=9, wrap="word", borderwidth=0)
        self.verdict_text.grid(row=0, column=1, sticky="nsew")
        self.verdict_text.insert("1.0", "Carga un cargo para calcular probabilidad.")
        self.verdict_text.configure(state="disabled")

        ttk.Label(right, text="Prompt para ChatGPT Free", style="Step.TLabel").grid(row=2, column=0, sticky="w")
        prompt_frame = ttk.Frame(right)
        prompt_frame.grid(row=3, column=0, sticky="nsew", pady=(6, 0))
        prompt_frame.columnconfigure(0, weight=1)
        prompt_frame.rowconfigure(0, weight=1)
        self.prompt_text = tk.Text(prompt_frame, wrap="word", undo=True)
        self.prompt_text.grid(row=0, column=0, sticky="nsew")
        prompt_scroll = ttk.Scrollbar(prompt_frame, orient="vertical", command=self.prompt_text.yview)
        prompt_scroll.grid(row=0, column=1, sticky="ns")
        self.prompt_text.configure(yscrollcommand=prompt_scroll.set)
        ttk.Button(right, text="Copiar prompt", command=self._copy_prompt).grid(row=4, column=0, sticky="e", pady=(8, 0))

    def _load_core_info(self) -> None:
        core = cv_app.load_core_documents()
        self.core_label.configure(
            text=(
                f"{core['cv_file']}: {len(core['cv'])} caracteres | "
                f"{core['experience_file']}: {len(core['experience'])} caracteres\n"
                "Para cambiar el master, reemplaza esos archivos en la carpeta core."
            )
        )

    def _load_job_list(self) -> None:
        jobs = cv_app.list_jobs()
        names = [job["name"] for job in jobs]
        self.job_combo.configure(values=names)
        if names:
            self.job_combo.current(0)

    def _load_selected_job(self) -> None:
        name = self.job_combo.get()
        if not name:
            messagebox.showinfo("Cargo", "No hay cargos en la carpeta jobs.")
            return
        path = cv_app.JOBS_DIR / Path(name).name
        self._set_job_text(cv_app.read_job_file(path))
        self.status_var.set(f"Cargo cargado: {name}")

    def _browse_job_file(self) -> None:
        filename = filedialog.askopenfilename(
            title="Selecciona descripcion de cargo",
            filetypes=[
                ("Cargos soportados", "*.txt *.md *.csv *.html *.htm *.docx"),
                ("Todos los archivos", "*.*"),
            ],
        )
        if not filename:
            return
        path = Path(filename)
        self._set_job_text(cv_app.read_job_file(path))
        self.status_var.set(f"Cargo cargado: {path.name}")

    def _set_job_text(self, value: str) -> None:
        self.job_text.delete("1.0", "end")
        self.job_text.insert("1.0", value)

    def _job_text_value(self) -> str:
        return self.job_text.get("1.0", "end").strip()

    def _evaluate_job(self) -> None:
        try:
            job_text = self._job_text_value()
            if not job_text:
                messagebox.showwarning("Falta cargo", "Pega o carga una descripcion del cargo primero.")
                return
            core = cv_app.load_core_documents()
            self.assessment = cv_app.assess_fit(core, job_text)
            self.ai_prompt = cv_app.build_ai_prompt(core, job_text, self.assessment)
            self._render_assessment()
            self._render_prompt()
            self.generate_button.configure(state="normal")
            self.status_var.set("Assessment listo. Decide si procede generar el paquete.")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def _generate_package(self) -> None:
        try:
            job_text = self._job_text_value()
            if not job_text:
                messagebox.showwarning("Falta cargo", "Pega o carga una descripcion del cargo primero.")
                return
            self.package = cv_app.build_application_package(job_text)
            self.assessment = self.package["assessment"]
            self.ai_prompt = self.package["ai_prompt"]
            self._render_assessment()
            self._render_prompt()
            files = "\n".join(item["file"] for item in self.package["files"])
            self.status_var.set("PDFs generados en output/pdf.")
            messagebox.showinfo("Paquete generado", f"Archivos generados:\n\n{files}")
            self._open_output_folder()
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def _render_assessment(self) -> None:
        if not self.assessment:
            return
        matched = ", ".join(self.assessment.get("matched_keywords") or [])
        missing = ", ".join(self.assessment.get("missing_keywords") or [])
        text = (
            f"{self.assessment['verdict']}\n\n"
            f"Recomendacion: {self.assessment['recommendation']}\n\n"
            f"Matched keywords:\n{matched or 'N/A'}\n\n"
            f"Missing keywords:\n{missing or 'N/A'}\n\n"
            f"{self.assessment['question']}"
        )
        self.score_label.configure(text=f"{self.assessment['score']}%")
        self.verdict_text.configure(state="normal")
        self.verdict_text.delete("1.0", "end")
        self.verdict_text.insert("1.0", text)
        self.verdict_text.configure(state="disabled")

    def _render_prompt(self) -> None:
        self.prompt_text.delete("1.0", "end")
        self.prompt_text.insert("1.0", self.ai_prompt)

    def _copy_prompt(self) -> None:
        text = self.prompt_text.get("1.0", "end").strip()
        if not text:
            return
        self.clipboard_clear()
        self.clipboard_append(text)
        self.status_var.set("Prompt copiado al portapapeles.")

    def _open_output_folder(self) -> None:
        cv_app.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        path = str(cv_app.OUTPUT_DIR)
        if sys.platform.startswith("win"):
            subprocess.Popen(["explorer", path])
        elif sys.platform == "darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])


def main() -> int:
    app = CVDesktopApp()
    app.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
