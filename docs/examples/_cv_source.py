# (kommiBo) Stdlib module load only; no core/job reads or application startup.
import importlib.util
from pathlib import Path
import sys
source = Path(__file__).resolve().parents[2] / 'cv-local-generator/cv_app.py'
spec = importlib.util.spec_from_file_location('synthetic_cv_source', source)
cv = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = cv
spec.loader.exec_module(cv)
