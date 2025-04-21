
import os
import subprocess

def run(target_folder):
    main_path = os.path.join(target_folder, "main_app.py")
    if not os.path.exists(main_path):
        return {
            "status": "FAIL",
            "error": "main_app.py not found, cannot run Streamlit app"
        }

    try:
        result = subprocess.run(
            ["streamlit", "run", main_path, "--server.headless=true"],
            cwd=target_folder,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=15,
            text=True
        )
        if result.returncode != 0:
            return {
                "status": "FAIL",
                "error": result.stderr[:500]  # Trim long output
            }
        return {
            "status": "PASS",
            "output": result.stdout[:500]
        }
    except Exception as e:
        return {
            "status": "FAIL",
            "exception": str(e)
        }
