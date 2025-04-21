
import os
import argparse
from run_audit import run_all_checks
from utils.logger import save_report
import json

def main():
    parser = argparse.ArgumentParser(description="Batch Audit for Multiple Streamlit Builds")
    parser.add_argument("--parent", type=str, required=True, help="Parent folder containing multiple Streamlit builds")
    args = parser.parse_args()

    parent_dir = args.parent
    builds = [d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))]

    for build in builds:
        path = os.path.join(parent_dir, build)
        print(f"Auditing: {build}")
        results = run_all_checks(path)

        report_dir = os.path.join("reports", build)
        os.makedirs(report_dir, exist_ok=True)

        with open(os.path.join(report_dir, "audit_log.json"), "w") as f:
            json.dump(results, f, indent=4)

        save_report(results, os.path.join(report_dir, "audit_report.md"))

if __name__ == "__main__":
    main()
