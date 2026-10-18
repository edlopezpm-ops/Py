# (kommiBo) Synthetic documentation example; no personal records.
from pathlib import Path
import subprocess
import sys
root = Path(__file__).resolve().parents[2]
script = root / 'Py Scripts/Practice2.py'
paths = {
    'direct': ('12345678\nY\n', None),
    'retry': ('abc\n12345678\n y \n', 'Container must be numeric'),
    'qc': ('12345678\nN\nY\nY\n', 'has been marked for QC'),
}
for name, (transcript, extra) in paths.items():
    result = subprocess.run([sys.executable, str(script)], input=transcript, text=True, capture_output=True, timeout=5)
    assert result.returncode == 0, result.stderr
    assert 'Process Completed: Container 12345678 is confirmed' in result.stdout
    if extra:
        assert extra in result.stdout
    print(f'{name}: confirmed')
