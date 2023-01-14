from typing import List
from .diff_tree_tools import (
    get_value, is_unchanged_items, is_changed_items,
    is_nested_structure, make_nested_structure,
    make_leaf_structure, make_changed_structure
)


def external_walk(dict_) -> List[dict]:
    diff = list()
    all_keys = [key for key in dict_]

    for key in all_keys:
        if is_nested_structure(key, dict_):
            child = get_value(dict_, key)
            children = external_walk(child)

            diff.append(make_nested_structure(key, 'unchanged', children))

            continue

        value = get_value(dict_, key)

        diff.append(make_leaf_structure(key, 'unchanged', value))

    return diff


def build_diff(data1: dict, data2: dict) -> List[dict]:
    diff = list()

    all_keys = sorted(
        set(data1) | set(data2)
    )

    for key in all_keys:

        if is_nested_structure(key, data1, data2):
            child1 = get_value(data1, key)
            child2 = get_value(data2, key)

            children = build_diff(child1, child2)

            diff.append(make_nested_structure(key, 'nested', children))

        elif is_unchanged_items(data1, data2, key):
            value = get_value(data1, key)

            diff.append(make_leaf_structure(key, 'unchanged', value))

        elif is_changed_items(data1, data2, key):
            values = list()

            if is_nested_structure(key, data1):
                children = external_walk(get_value(data1, key))
                values.append(children)

            else:
                value1 = get_value(data1, key)
                values.append(value1)

            if is_nested_structure(key, data2):
                children = external_walk(get_value(data2, key))
                values.append(children)

            else:
                value2 = get_value(data2, key)
                values.append(value2)

            diff.append(make_changed_structure(key, values))

        elif key in data1:
            if is_nested_structure(key, data1):
                children = external_walk(get_value(data1, key))

                diff.append(make_nested_structure(key, 'deleted', children))

            else:
                value = get_value(data1, key)

                diff.append(make_leaf_structure(key, 'deleted', value))

        elif key in data2:
            if is_nested_structure(key, data2):
                children = external_walk(get_value(data2, key))

                diff.append(make_nested_structure(key, 'added', children))

            else:
                value = get_value(data2, key)

                diff.append(make_leaf_structure(key, 'added', value))

    return diff


def build_diff_tree(data1, data2):
    return {
        'type': 'diff',
        'children': build_diff(data1, data2),
    }
