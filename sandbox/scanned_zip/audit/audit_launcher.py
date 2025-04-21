import audit.level1_structure as l1
import audit.level2_placeholder as l2
import audit.level3_imports as l3
import audit.level4_function_calls as l4
import audit.level5_functional_runner as l5

def run_all():
    results = {}
    results['L1'] = l1.run()
    results['L2'] = l2.run()
    results['L3'] = l3.run()
    results['L4'] = l4.run()
    results['L5'] = l5.run()

    with open("logs/audit_log.json", "w") as f:
        import json
        json.dump(results, f, indent=2)

    with open("logs/audit_report.md", "w") as f:
        for level, passed in results.items():
            emoji = "✅" if passed else "❌"
            f.write(f"{emoji} {level} Audit {'Passed' if passed else 'Failed'}\n")

if __name__ == "__main__":
    run_all()