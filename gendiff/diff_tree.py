from typing import List


def build_diff(data1: dict, data2: dict) -> List[dict]:
    diff = list()

    all_keys = sorted(
        set(data1) | set(data2)
    )

    for key in all_keys:
        if key not in data2:
            diff.append({
                'key': key,
                'type': 'deleted',
                'value': data1[key]
            })

        elif key not in data1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = build_diff(data1[key], data2[key])

            diff.append({
                'key': key,
                'type': 'nested',
                'children': children
            })

        elif data1[key] != data2[key]:
            diff.append({
                'key': key,
                'type': 'changed',
                'value1': data1[key],
                'value2': data2[key]
            })

        else:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key]
            })

    return diff


def build_diff_tree(data1, data2):
    return {
        'type': 'diff',
        'children': build_diff(data1, data2),
    }
