def normalize_bool(value, mode='not_plain'):
    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'

    elif value is None:
        return 'null'

    if mode == 'plain':
        if isinstance(value, list):
            return '[complex value]'

        elif value in ('true', 'false', 'null'):
            return value

        return f"'{value}'"

    return value


def get_value(items: dict, key: str):
    return items[key]


def get_status(status: str):
    statuses = {
        'added': '  + ',
        'deleted': '  - ',
        'nested': '    ',
        'unchanged': '    '
    }
    return statuses[status]


def is_nested_structure(value, *dictionaries):
    if len(dictionaries) == 2:
        first_file, second_file = dictionaries

        if value in first_file and value in second_file:
            return (
                isinstance(get_value(first_file, value), dict)
                and isinstance(get_value(second_file, value), dict)
            )
        return False

    if dictionaries == ():
        return isinstance(value, dict)

    file = dictionaries[0]

    return isinstance(file[value], dict)


def is_unchanged_items(first_file, second_file, key):
    if key in first_file and key in second_file:
        if get_value(first_file, key) == get_value(second_file, key):
            return True
    return False


def is_changed_items(first_file, second_file, key):
    return key in first_file and key in second_file


def make_leaf_structure(key, type, value):
    return {'key': key, 'type': type, 'value': value}


def make_nested_structure(key, type, children):
    return {'key': key, 'type': type, 'children': children}


def make_changed_structure(key, values):
    result = {'key': key, 'type': 'changed'}

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
