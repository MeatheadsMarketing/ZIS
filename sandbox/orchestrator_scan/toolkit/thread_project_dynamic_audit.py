import os
import json
from pathlib import Path

SEARCH_ROOT = Path.cwd()
THREAD_NAMES = ["ThreadFullSpectrumExtraction_v1.1", "ThreadRecoveryOrganizer_v1.1"]

REQUIRED_STRUCTURE = {
    "engine": ["*.py"],
    "interface": ["main_app.py", "*.py"],
    "exports": ["*.md", "*.csv", "*.json"],
    "data": ["*.csv"],
    "docs": ["README.md"]
}

def find_thread_directories():
    found = []
    for name in THREAD_NAMES:
        for path in SEARCH_ROOT.rglob("*"):
            if path.name == name and path.is_dir():
                found.append(path.resolve())
                break
    return found

def check_folder_structure(base):
    results = {"folder": str(base), "checks": {}, "missing": [], "empty": [], "summary": ""}
    for subdir, patterns in REQUIRED_STRUCTURE.items():
        path = base / subdir
        if not path.exists():
            results["missing"].append(str(path))
            results["checks"][subdir] = "❌ Missing Folder"
            continue
        results["checks"][subdir] = []
        for pattern in patterns:
            matches = list(path.glob(pattern))
            if not matches:
                results["checks"][subdir].append(f"❌ Missing: {pattern}")
            else:
                for match in matches:
                    if match.stat().st_size == 0:
                        results["empty"].append(str(match))
                        results["checks"][subdir].append(f"⚠️ Empty: {match.name}")
                    else:
                        results["checks"][subdir].append(f"✅ {match.name}")
    total_issues = len(results["missing"]) + len(results["empty"])
    results["summary"] = "✅ All checks passed" if total_issues == 0 else f"⚠️ {total_issues} issues found"
    return results

def run_dynamic_audit():
    thread_dirs = find_thread_directories()
    if not thread_dirs:
        print("❌ No valid thread directories found.")
        return
    full_report = []
    for root in thread_dirs:
        result = check_folder_structure(root)
        full_report.append(result)
    output = Path("audit_results_dynamic.json")
    output.write_text(json.dumps(full_report, indent=2))
    print("✅ Audit complete. Report saved to 'audit_results_dynamic.json'.")

if __name__ == "__main__":
    run_dynamic_audit()