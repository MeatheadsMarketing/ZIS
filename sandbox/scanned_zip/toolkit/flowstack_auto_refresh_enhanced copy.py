import os
import time
import pandas as pd
import subprocess

CSV_PATH = "flowstack_master_v5.csv"
MD_PATH = "flowstack_map.md"
PLACEHOLDER_COLUMN = "Placeholder Check"

def generate_mermaid_from_csv(csv_path=CSV_PATH, output_path=MD_PATH):
    df = pd.read_csv(csv_path)
    mermaid_lines = ["```mermaid", "graph TD"]

    for _, row in df.iterrows():
        name = row["Name"]
        level = row["Flow Level"]
        upstream = str(row["Upstream Dependencies"]).split(";") if pd.notna(row["Upstream Dependencies"]) else []

        for dep in upstream:
            if dep.strip():
                mermaid_lines.append(f'    "{dep.strip()}" --> "{name}"')

        if level == 1:
            mermaid_lines.append(f'    class "{name}" level1;')
        elif level == 2:
            mermaid_lines.append(f'    class "{name}" level2;')
        elif level == 3:
            mermaid_lines.append(f'    class "{name}" level3;')
        elif level == 4:
            mermaid_lines.append(f'    class "{name}" level4;')
        elif level == 5:
            mermaid_lines.append(f'    class "{name}" level5;')

    mermaid_lines += [
        "    classDef level1 fill:#f9f,stroke:#333,stroke-width:2px;",
        "    classDef level2 fill:#bbf,stroke:#333,stroke-width:2px;",
        "    classDef level3 fill:#bfb,stroke:#333,stroke-width:2px;",
        "    classDef level4 fill:#fbf,stroke:#333,stroke-width:2px;",
        "    classDef level5 fill:#ffb,stroke:#333,stroke-width:2px;",
        "```"
    ]

    with open(output_path, "w") as f:
        f.write("\n".join(mermaid_lines))

    print(f"Mermaid map updated: {output_path}")

def check_for_placeholders(csv_path=CSV_PATH):
    df = pd.read_csv(csv_path)
    if PLACEHOLDER_COLUMN in df.columns:
        flagged = df[df[PLACEHOLDER_COLUMN] == True]
        if not flagged.empty:
            print(f"⚠️ Detected {len(flagged)} placeholder rows. Recommend rebuild.")
        else:
            print("✅ No placeholder logic detected.")
    else:
        print("⚠️ Placeholder Check column not found.")

def auto_commit_and_tag():
    try:
        subprocess.run(["git", "add", CSV_PATH, MD_PATH], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-update: FlowStack refreshed with new map"], check=True)
        subprocess.run(["git", "tag", "flowstack-auto-refresh"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--tags"], check=True)
        print("✅ Git commit and tag pushed.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")

def auto_refresh_loop(interval_sec=60):
    print(f"Auto-refresh started. Updating every {interval_sec} seconds.")
    while True:
        generate_mermaid_from_csv()
        check_for_placeholders()
        auto_commit_and_tag()
        time.sleep(interval_sec)

if __name__ == "__main__":
    auto_refresh_loop()
