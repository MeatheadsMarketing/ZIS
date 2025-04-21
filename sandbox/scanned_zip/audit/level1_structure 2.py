import os

REQUIRED_FOLDERS = ['assistant_core', 'tools', 'config', 'ui_layer', 'validation', 'audit', 'logs', 'data']
REQUIRED_FILES = ['README.md', 'vault_mode.json']

def run():
    print("📁 Level 1 Audit – Structure Check")
    passed = True
    for folder in REQUIRED_FOLDERS:
        if not os.path.isdir(folder):
            print(f"❌ Missing folder: {folder}")
            passed = False
    for file in REQUIRED_FILES:
        if not os.path.isfile(file):
            print(f"❌ Missing file: {file}")
            passed = False
    if passed:
        print("✅ Level 1 Passed: All required folders/files are present.")
    return passed