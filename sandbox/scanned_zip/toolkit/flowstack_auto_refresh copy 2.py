import time
import pandas as pd

CSV_PATH = "flowstack_master_v5.csv"
MD_PATH = "flowstack_map.md"

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

def auto_refresh_loop(interval_sec=60):
    print(f"Auto-refresh started. Updating every {interval_sec} seconds.")
    while True:
        generate_mermaid_from_csv()
        time.sleep(interval_sec)

if __name__ == "__main__":
    auto_refresh_loop()
