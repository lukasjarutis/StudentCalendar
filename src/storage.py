import json
import os


def save_schedule(path: str, model):
    data = model.to_dict()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_schedule(path: str, model):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with open(path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    model.from_dict(payload)
