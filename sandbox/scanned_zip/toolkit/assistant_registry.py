
import csv
import os

REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "assistant_registry.csv")

def load_registry():
    registry = {}
    if not os.path.exists(REGISTRY_PATH):
        return registry
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = row.get("Code") or row.get("Assistant")
            if code:
                registry[code] = row
    return registry
