import json


def diff_to_json(diff):
    return json.dumps(diff, indent=2)
