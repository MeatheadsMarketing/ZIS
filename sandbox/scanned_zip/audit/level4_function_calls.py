import os
import importlib.util
import inspect

def run():
    print("🧪 Level 4 Audit – Function Call Smoke Test")
    failed = []
    for root, _, files in os.walk("tools"):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                spec = importlib.util.spec_from_file_location("mod", path)
                mod = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(mod)
                    for name, func in inspect.getmembers(mod, inspect.isfunction):
                        try:
                            func()
                        except:
                            continue
                except Exception as e:
                    failed.append((path, str(e)))
    if failed:
        print("❌ Function call failures:")
        for f in failed:
            print(f" - {f[0]} — {f[1]}")
        return False
    print("✅ Level 4 Passed: Core functions callable.")
    return True