import os

def run():
    print("⚠️ Level 2 Audit – Placeholder Detection")
    issues = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if 'TODO' in content or 'pass' in content or len(content.strip()) < 20:
                        issues.append(path)
    if issues:
        print("❌ Placeholder code detected in:")
        for i in issues:
            print(f" - {i}")
        return False
    print("✅ Level 2 Passed: No placeholder logic found.")
    return True