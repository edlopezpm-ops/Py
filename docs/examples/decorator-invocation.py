# (kommiBo) Synthetic documentation example; no personal records.
import contextlib
import io
from pathlib import Path
import runpy
root = Path(__file__).resolve().parents[2]
with contextlib.redirect_stdout(io.StringIO()):
    values = runpy.run_path(str(root / 'Py Scripts/decoradores.py'))
output = io.StringIO()
with contextlib.redirect_stdout(output):
    result = values['sum'](2, 3)
assert result == 5
assert output.getvalue().strip() == 'Name: Nombre Decorador'
assert values['sum'].__name__ == 'envolvedor'
print('wrapper: Name: Nombre Decorador; return: 5; metadata name: envolvedor')
