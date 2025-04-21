import json
import pandas as pd

def build_meta_index(file_df):
    meta_json = file_df.to_dict(orient="records")
    meta_csv = file_df.to_csv(index=False)
    return meta_csv, json.dumps(meta_json, indent=2)