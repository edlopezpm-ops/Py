# (kommiBo) Synthetic documentation example; no personal records.
import ast
from pathlib import Path
root = Path(__file__).resolve().parents[2]
tree = ast.parse((root / 'DataAnalyticsPy/ImportPandas.py').read_text(encoding='utf-8'))
assert any(isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'read_fwf' for n in ast.walk(tree))
rows = [('S001', '12'), ('S002', '7')]
report = 'SHIPMENT  UNITS\n' + '\n'.join(f'{shipment:<10}{units}' for shipment, units in rows)
parsed = [(line[:10].strip(), int(line[10:])) for line in report.splitlines()[1:]]
assert parsed == [('S001', 12), ('S002', 7)]
assert sum(units for _, units in parsed) == 19
print(report)
print('two synthetic rows; total units=19; profiling source not imported')
