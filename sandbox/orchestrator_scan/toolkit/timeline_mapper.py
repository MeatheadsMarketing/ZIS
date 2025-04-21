import pandas as pd
import altair as alt
from pathlib import Path

def generate_timeline(base_path: Path):
    file_data = []
    for filepath in base_path.rglob("*"):
        if filepath.is_file():
            file_data.append({
                "filename": filepath.name,
                "timestamp": filepath.stat().st_mtime
            })
    df = pd.DataFrame(file_data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s')
    return alt.Chart(df).mark_bar().encode(
        x='timestamp:T',
        y='filename:N',
        tooltip=['filename', 'timestamp']
    ).properties(height=300)