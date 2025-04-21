import subprocess

def run():
    print("🚀 Level 5 Audit – Functional Flow Test")
    try:
        subprocess.run(["python", "config/test_keychain.py"], check=True)
        print("✅ Level 5 Passed: Assistant core system is functional.")
        return True
    except subprocess.CalledProcessError:
        print("❌ Level 5 Failed: Functional run crashed.")
        return False