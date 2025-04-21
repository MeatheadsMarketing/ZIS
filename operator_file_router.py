
import os
import json
from pathlib import Path

# Local-run version; user plugs in GPT key and call logic
def prepare_operator_prompts(scan_dir, output_path="outputs/operator_prompt_queue.json"):
    files = []

    for filepath in Path(scan_dir).rglob("*.*"):
        if filepath.suffix not in [".py", ".md", ".json"]:
            continue

        content = filepath.read_text(encoding="utf-8", errors="ignore")[:3000]
        files.append({
            "file": filepath.name,
            "type": filepath.suffix,
            "path": str(filepath),
            "preview": content
        })

    prompts = []
    for f in files:
        prompt = f"""You are an intelligent routing assistant for a GPT-powered assistant recovery system.

Your job is to classify this file:
- Name: {f['file']}
- Type: {f['type']}
- Preview:
{f['preview'][:800]}

Routing Destinations:
1. 🧠 GPT Orchestrator
2. 🧠 Auto-Tagger
3. 📦 Export Launcher
4. 📝 README Generator
5. 📋 Registry Viewer
6. 🧠 GPT Notes Viewer
7. 📜 Recovery Timeline
8. ❌ Skip (no action needed)

Reply in this JSON format:

{{
  "file": "{f['file']}",
  "route": "[destination]",
  "reason": "..."
}}
""" 
        prompts.append({
            "file": f["file"],
            "path": f["path"],
            "prompt": prompt
        })

    os.makedirs("outputs", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(prompts, f, indent=2)

    print(f"Prompts saved to {output_path}")

# Example usage:
# prepare_operator_prompts('sandbox/inspect_toolkit')

prepare_operator_prompts("sandbox/inspect_toolkit")
