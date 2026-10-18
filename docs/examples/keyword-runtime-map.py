# (kommiBo) Synthetic documentation example; no personal records.
import ast
import keyword
from pathlib import Path
root = Path(__file__).resolve().parents[2]
def dictionary(path, name):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in n.targets))
    return ast.literal_eval(node.value)
sample = dictionary(root / 'Py Scripts/SampleKeywords.py', 'explicaciones')
master = dictionary(root / 'Py Scripts/MasterPyKWs.py', 'keywords')
assert sample['return'] and master['return']
assert keyword.iskeyword('return') and not keyword.iskeyword('match')
assert keyword.issoftkeyword('match')
print('return: reserved; match: soft keyword; explanatory maps loaded without input')
print('unexplained reserved keywords:', ', '.join(sorted(set(keyword.kwlist) - set(sample))) or 'none')
