
import os
import argparse
import json
from datetime import datetime
from checks import file_structure_check, placeholder_scan, ui_integrity_check, streamlit_run_check, manifest_validator, performance_check
from utils.logger import log_result, save_report

def run_all_checks(target_folder):
    results = {}

    results["structure"] = file_structure_check.run(target_folder)
    results["placeholders"] = placeholder_scan.run(target_folder)
    results["ui"] = ui_integrity_check.run(target_folder)
    results["runtime"] = streamlit_run_check.run(target_folder)
    results["manifest"] = manifest_validator.run(target_folder)
    results["performance"] = performance_check.run(target_folder)

    return results

def main():
    parser = argparse.ArgumentParser(description="Run Level 5 Streamlit Audit.")
    parser.add_argument('--target', type=str, required=True, help='Target Streamlit project folder')
    args = parser.parse_args()

    results = run_all_checks(args.target)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    report_dir = os.path.join("reports", os.path.basename(args.target))
    os.makedirs(report_dir, exist_ok=True)

    # Save JSON log
    with open(os.path.join(report_dir, "audit_log.json"), "w") as f:
        json.dump(results, f, indent=4)

    # Save Markdown report
    save_report(results, os.path.join(report_dir, "audit_report.md"))

if __name__ == "__main__":
    main()
