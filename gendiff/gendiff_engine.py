from .tools import (
    get_value, is_unchanged_items,
    is_changed_items, is_nested_structure,
    normalize_bool, make_nested_structure,
    make_leaf_structure, make_changed_structure
)


def external_walk(dict_):
    diff = list()
    all_keys = [key for key in dict_]

    for key in all_keys:
        if is_nested_structure(key, dict_):
            child = get_value(dict_, key)
            children = external_walk(child)

            diff.append(make_nested_structure('unchanged', key, children))

            continue

        value = normalize_bool(get_value(dict_, key))

        diff.append(make_leaf_structure('unchanged', key, value))

    return diff


def build_diff(file_1: dict, file_2: dict):
    diff = list()

    all_keys = sorted(
                    [key for key in file_1] +
                    [key for key in file_2 if key not in file_1]
    )

    for key in all_keys:

        if is_nested_structure(key, file_1, file_2):
            child1 = get_value(file_1, key)
            child2 = get_value(file_2, key)

            children = build_diff(child1, child2)

            diff.append(make_nested_structure('nested', key, children))


        elif is_unchanged_items(file_1, file_2, key):
            value = normalize_bool(get_value(file_1, key))

            diff.append(make_leaf_structure('unchanged', key, value))


        elif is_changed_items(file_1, file_2, key):
            values = list()

            if is_nested_structure(key, file_1):
                children = external_walk(get_value(file_1, key))
                values.append(children)

            else:
                value1 = normalize_bool(get_value(file_1, key))
                values.append(value1)

            if is_nested_structure(key, file_2):
                children = external_walk(get_value(file_2, key))
                values.append(children)

            else:
                value2 = normalize_bool(get_value(file_2, key))
                values.append(value2)

            diff.append(make_changed_structure(key, values))


        elif key in file_1:
            if is_nested_structure(key, file_1):
                children = external_walk(get_value(file_1, key))

                diff.append(make_nested_structure('deleted', key, children))

            else:
                value = normalize_bool(get_value(file_1, key))

                diff.append(make_leaf_structure('deleted', key, value))


        elif key in file_2:
            if is_nested_structure(key, file_2):
                children = external_walk(get_value(file_2, key))

                diff.append(make_nested_structure('added', key, children))

            else:
                value = normalize_bool(get_value(file_2, key))

                diff.append(make_leaf_structure('added', key, value))

    return diff
