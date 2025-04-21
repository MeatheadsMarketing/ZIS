
import datetime

REPLAY_LOG_PATH = "outputs/router_replay_log.json"

def append_replay_log(file, action, route, reason):
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "file": file,
        "action": action,
        "route": route,
        "reason": reason
    }
    if os.path.exists(REPLAY_LOG_PATH):
        with open(REPLAY_LOG_PATH, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []
    history.append(log_entry)
    with open(REPLAY_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
