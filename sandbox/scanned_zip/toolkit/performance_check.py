
import os
import time
import importlib.util

def time_run_ui(file_path):
    try:
        start = time.time()
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "run_ui"):
            module.run_ui()
        duration = time.time() - start
        return round(duration, 3)
    except Exception as e:
        return f"ERROR: {str(e)}"

def run(target_folder):
    times = {}
    for root, _, files in os.walk(target_folder):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                t = time_run_ui(path)
                times[path] = t

    errors = {k: v for k, v in times.items() if isinstance(v, str) and v.startswith("ERROR")}
    slow = {k: v for k, v in times.items() if isinstance(v, float) and v > 2.0}

    return {
        "status": "FAIL" if errors or slow else "PASS",
        "slow_files": slow,
        "errors": errors
    }
