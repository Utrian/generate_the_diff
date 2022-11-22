from os.path import abspath
from json import load as json_load
from yaml import load as yaml_load, Loader as yaml_Loader


def get_files(args) -> tuple:
    abs_path_first_file = abspath(args.first_file)
    abs_path_second_file = abspath(args.second_file)

    first_file_format = abs_path_first_file.split('.')[1]
    second_file_format = abs_path_second_file.split('.')[1]

    if first_file_format == 'json':
        first_file = json_load(open(abs_path_first_file))

    elif first_file_format in ['yml', 'yaml']:
        first_file = yaml_load(open(abs_path_first_file), Loader=yaml_Loader)

    if second_file_format == 'json':
        second_file = json_load(open(abs_path_second_file))

    elif second_file_format in ['yml', 'yaml']:
        second_file = yaml_load(open(abs_path_second_file), Loader=yaml_Loader)

    return first_file, second_file


def normalize_bool(value):
    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'

    if value is None:
        return 'null'

    return value


def get_value(file, key):
    return normalize_bool(file[key])


def get_operation(status):
    OPERATIONS = {
        'equal': '    ',
        'added': '  + ',
        'deleted': '  - '
    }
    return OPERATIONS[status]


def get_inner_data(key, status, depth, value):
    return {
        'key': key,
        'status': status,
        'depth': depth,
        'value': value,
    }


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
        return isinstance(value, list)

    file = files[0]

    return isinstance(file[key], dict)


def is_equal_items(first_file, second_file, key):
    if key in first_file and key in second_file:
        if get_value(first_file, key) == get_value(second_file, key):
            return True
    return False
