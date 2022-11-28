import json


def diff_to_json(diff: dict):
    return json.dumps(diff, indent=2)
