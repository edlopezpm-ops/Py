from __future__ import annotations

import ast
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRECTORIES = {".git", ".venv", "venv", "__pycache__"}


def repository_files(pattern: str) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob(pattern)
        if not IGNORED_DIRECTORIES.intersection(path.relative_to(ROOT).parts)
    )


class RepositoryContractTests(unittest.TestCase):
    def test_every_python_source_parses(self) -> None:
        sources = repository_files("*.py")
        self.assertTrue(sources, "expected at least one Python source file")

        for path in sources:
            with self.subTest(path=path.relative_to(ROOT)):
                source = path.read_text(encoding="utf-8")
                ast.parse(source, filename=str(path))

    def test_every_json_document_loads(self) -> None:
        documents = repository_files("*.json")
        self.assertTrue(documents, "expected at least one JSON document")

        for path in documents:
            with self.subTest(path=path.relative_to(ROOT)):
                json.loads(path.read_text(encoding="utf-8"))

    def test_documented_entry_points_exist(self) -> None:
        required_paths = (
            ROOT / "README.md",
            ROOT / "Run-CVGenerator.ps1",
            ROOT / "cv-local-generator" / "README.md",
            ROOT / "cv-local-generator" / "cv_app.py",
            ROOT / "cv-local-generator" / "desktop_app.py",
            ROOT / ".github" / "workflows" / "validation.yml",
        )

        for path in required_paths:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertTrue(path.is_file(), f"required path is missing: {path}")


if __name__ == "__main__":
    unittest.main()
