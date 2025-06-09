from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "main"

for json_path in sorted(DATA_DIR.rglob("*.json")):
    df = pd.read_json(json_path)
    print(f"\n=== {json_path.relative_to(DATA_DIR.parent)} ===")
    print(df.iloc[0])
