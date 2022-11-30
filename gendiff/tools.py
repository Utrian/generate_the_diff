def normalize_bool(value):
    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'

    if value is None:
        return 'null'

    return value


def get_value(items: dict, key: str):
    return items[key]


def get_status(status: str):
    statuses = {
        'added': '  + ',
        'deleted': '  - ',
        'nested': '    ',
        'unchanged': '    ',
        'changed': ('  - ', '  + ')
    }
    return statuses[status]


def is_nested_structure(key, *files):
    if len(files) == 2:
        first_file, second_file = files

        if key in first_file and key in second_file:
            return (
                isinstance(get_value(first_file, key), dict) and
                isinstance(get_value(second_file, key), dict)
            )
        return False

    if files == ():
        value = key
        return isinstance(value, dict)

    file = files[0]

    return isinstance(file[key], dict)


def is_unchanged_items(first_file, second_file, key):
    if key in first_file and key in second_file:
        if get_value(first_file, key) == get_value(second_file, key):
            return True
    return False


def is_changed_items(first_file, second_file, key):
    return key in first_file and key in second_file


def make_leaf_structure(type, key, value):
    return {'type': type, 'key': key, 'value': value}


def make_nested_structure(type, key, children):
    return {'type': type, 'key': key, 'children': children}


def make_changed_structure(key, values):
    result = {'type': 'changed', 'key': key}

    if isinstance(values[0], list):
        value1 = {'children': values[0]}
    else:
        value1 = {'value1': values[0]}

    if isinstance(values[1], list):
        value2 = {'children': values[1]}
    else:
        value2 = {'value2': values[1]}

    result.update(value1)
    result.update(value2)

    return result
