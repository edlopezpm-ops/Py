import pandas as pd
from pathlib import Path

try:
    from data_profiling import ProfileReport
except ModuleNotFoundError:
    from ydata_profiling import ProfileReport

BASE_DIR = Path(__file__).parent

file_path = BASE_DIR / "data" / "Shipment Duplicated.rpt"
output_path = BASE_DIR / "output" / "Shipment Duplicated.html"

df = pd.read_fwf(file_path, encoding="utf-8")

print(df.head())
print(df.shape)
print(df.info())

profile = ProfileReport(df, title="SQL RPT Profiling", explorative=True)
profile.to_file(output_path)

print(f"Profile created: {output_path}")
