import json


def diff_to_json(tree: list):
    diff = tree['children']
    return json.dumps(diff)
