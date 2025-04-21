import os
import importlib.util

def run():
    print("📦 Level 3 Audit – Import Integrity")
    passed = True
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py") and '__' not in file:
                module_path = os.path.join(root, file)
                spec = importlib.util.spec_from_file_location("mod", module_path)
                try:
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                except Exception as e:
                    print(f"❌ Import failed: {module_path} — {e}")
                    passed = False
    if passed:
        print("✅ Level 3 Passed: All imports succeeded.")
    return passed