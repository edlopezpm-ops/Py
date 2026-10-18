# (kommiBo) Synthetic documentation example; no personal records.
import contextlib
import io
from pathlib import Path
import runpy
root = Path(__file__).resolve().parents[2]
with contextlib.redirect_stdout(io.StringIO()):
    values = runpy.run_path(str(root / 'Py Scripts/Practice.py'))
results = tuple(values[name] for name in ('result1', 'result2', 'result3'))
assert results == (2.5, 6.25, 14.5)
assert bool(results[0] + results[2]) is True
assert bool(0) is False
assert values['elegir_mensaje'](*results).endswith('-->> 17.0')
print('results=(2.5, 6.25, 14.5); sum=17.0; zero is false')
