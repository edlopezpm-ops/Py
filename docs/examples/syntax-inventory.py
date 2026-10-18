# (kommiBo) Synthetic documentation example; no personal records.
import ast
from pathlib import Path
root = Path(__file__).resolve().parents[2]
paths = [root / 'Py Scripts/Practice2.py', root / 'DataAnalyticsPy/ImportPandas.py', root / 'cv-local-generator/cv_app.py']
for path in paths:
    tree = ast.parse(path.read_text(encoding='utf-8'))
    assert any(isinstance(node, ast.Call) for node in ast.walk(tree))
    print(f'{path.relative_to(root).as_posix()}: parsed; call sites present')
print('No application entry point executed')
