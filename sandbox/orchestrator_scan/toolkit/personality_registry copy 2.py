import json

def register_profile(profile, filename="persona_registry.json"):
    with open(filename, "a") as f:
        f.write(json.dumps(profile) + "\n")
    return filename