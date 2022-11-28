def normalize_bool(value):
    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'

    if value is None:
        return 'null'

    return value


def get_value(file, key):
    return file[key]


def get_status(status):
    statuses = {
        'equal': '    ',
        'added': '  + ',
        'deleted': '  - '
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


def is_equal_items(first_file, second_file, key):
    if key in first_file and key in second_file:
        if get_value(first_file, key) == get_value(second_file, key):
            return True
    return False


def is_not_equal_items(first_file, second_file, key):
    return key in first_file and key in second_file
