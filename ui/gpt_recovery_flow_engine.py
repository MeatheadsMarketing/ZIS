
import os
import pandas as pd
import shutil
from pathlib import Path
from gpt_logic_evaluator import set_api_key, gpt_analyze_script

REGISTRY_PATH = "registry/component_registry.csv"
SHORTCUT_PATH = "shortcuts/shortcut_registry_batch_05.csv"
EXPORT_DIR = "exports/"
TOOL_LIB = "RecoveredTools_Library_Categorized"

def recover_and_register(component_file, category, gpt_tag="", force_role=""):
    # Load file content
    found = None
    for root, _, files in os.walk(TOOL_LIB):
        if component_file in files:
            found = os.path.join(root, component_file)
            break

    if not found:
        return f"File {component_file} not found in tool library."

    with open(found, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

    set_api_key()
    notes = gpt_tag or gpt_analyze_script(code)

    role = force_role or "Utility"
    for r in ["Cleaner", "Trigger", "Planner", "Auditor", "Utility"]:
        if r.lower() in notes.lower():
            role = r
            break

    row = {
        "Component": component_file,
        "Type": "Recovered Tool",
        "Origin": category,
        "Status": "Launch-Ready",
        "Tags": role,
        "Shortcut": f"#{component_file.replace('.py','').upper()}",
        "GPT_Notes": notes
    }

    if os.path.exists(REGISTRY_PATH):
        df = pd.read_csv(REGISTRY_PATH)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])
    df.to_csv(REGISTRY_PATH, index=False)

    return f"✅ Registered {component_file} as {role}."

def export_tool_zip(component_list, pack_name="gpt_pack"):
    out_dir = f"{EXPORT_DIR}/{pack_name}"
    os.makedirs(out_dir, exist_ok=True)
    copied = []

    for tool in component_list:
        found = None
        for root, _, files in os.walk(TOOL_LIB):
            if tool in files:
                found = os.path.join(root, tool)
                break
        if found:
            shutil.copy(found, os.path.join(out_dir, tool))
            copied.append(tool)

    zip_path = shutil.make_archive(out_dir, "zip", out_dir)
    return f"📦 Exported {len(copied)} files to `{zip_path}`"

def suggest_shortcut_row(component_file, optional_tag=""):
    return {
        "Shortcut": f"#{component_file.replace('.py','').upper()}",
        "Component": component_file,
        "Tag": optional_tag or "Unassigned"
    }
