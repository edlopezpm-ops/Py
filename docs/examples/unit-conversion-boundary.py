# (kommiBo) Synthetic documentation example; no personal records.
import contextlib
import io
from pathlib import Path
import runpy
root = Path(__file__).resolve().parents[2]
with contextlib.redirect_stdout(io.StringIO()):
    values = runpy.run_path(str(root / 'Py Scripts/Practice.py'))
assert values['T_QTY'] == 800
assert values['T_QTY'] * values['HundredWeight'] == 160.0
def sample_charge(quantity, unit):
    total = quantity * values['UOM'][unit]
    return total * values['HundredWeight'] if total > 100 else 0
assert sample_charge(10, 'CS') == 0
assert sample_charge(11, 'CS') == 22.0
try:
    sample_charge(1, 'UNKNOWN')
except KeyError:
    pass
else:
    raise AssertionError('Unknown unit should require an explicit mapping')
print('800 units -> 160.0; 100 -> 0; 110 -> 22.0; unknown unit rejected')
