# (kommiBo) Synthetic documentation example; no personal records.
import contextlib
import io
from pathlib import Path
import runpy
root = Path(__file__).resolve().parents[2]
with contextlib.redirect_stdout(io.StringIO()):
    values = runpy.run_path(str(root / 'Py Scripts/BuildIns.py'))
assert values['dic2']['llave1']['metallave1']['metametallave1_2'] == 'valor metametallave1_2'
counts = values['lista_diccionario']
assert counts == {'v1': 3, 'v2': 1, 'v3': 2, 'v4': 1}
assert sum(counts.values()) == len(values['lista']) == 7
assert counts.get('missing', 0) == 0
assert 'missing' not in counts
print('four distinct values; seven observations; v1=3; missing defaults to zero')
