# (kommiBo) Synthetic documentation example; no personal records.
import importlib.util
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('synthetic_greeting', root / 'Py Scripts/HelloWordOverEng.py')
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
class PlainRenderer:
    def renderizar(self, mensaje):
        return mensaje.texto.upper()
message = module.Mensaje('sample', module.Idioma.ESPANOL)
assert module.ServicioSaludo(PlainRenderer()).ejecutar(message) == 'SAMPLE'
assert module.ServicioSaludo(module.RenderizadorConsola()).ejecutar(message) == '[ES] >>> sample'
try:
    module.ServicioSaludo(PlainRenderer()).ejecutar(module.Mensaje('', module.Idioma.ESPANOL))
except ValueError:
    print('injected: SAMPLE; console: [ES] >>> sample; empty rejected')
else:
    raise AssertionError('Empty message accepted')
