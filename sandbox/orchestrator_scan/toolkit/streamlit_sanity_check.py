import os
import importlib.util
import traceback

REQUIRED_FILES = [
    "main_app.py",
    "tab_flowstack_tracker.py",
    "tab_flowstack_visual.py",
    "tab_flowstack_validator.py"
]

def check_file_exists(filename):
    if not os.path.exists(filename):
        print(f"❌ MISSING: {filename}")
        return False
    print(f"✅ Found: {filename}")
    return True

def check_run_ui_function(filepath):
    try:
        spec = importlib.util.spec_from_file_location("module.name", filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "run_ui"):
            print(f"✅ {filepath} has run_ui()")
            return True
        else:
            print(f"❌ {filepath} is missing run_ui()")
            return False
    except Exception as e:
        print(f"❌ Error loading {filepath}: {e}")
        traceback.print_exc()
        return False

def sanity_check():
    print("🔍 Running Streamlit sanity check...")

    all_good = True
    for f in REQUIRED_FILES:
        if not check_file_exists(f):
            all_good = False
        elif f.endswith(".py"):
            if not check_run_ui_function(f):
                all_good = False

    if all_good:
        print("\n🎯 Streamlit build is VALID.")
    else:
        print("\n🚨 Streamlit build has ERRORS.")

if __name__ == "__main__":
    sanity_check()
