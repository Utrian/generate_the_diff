from os.path import abspath
from json import load as json_load
from yaml import load as yaml_load, Loader as yaml_Loader
from gendiff.tools.parser import parser


def get_files() -> tuple:
    args = parser()

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


def get_first_file():
    return get_files()[0]


def get_second_file():
    return get_files()[1]


def normalize_bool(value):
    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'
    return value


def get_item(file, key):
    return normalize_bool(file[key])


def get_operation(operation):
    OPERATIONS = {
        'Equal': '    ',
        'Delete': '  - ',
        'Adding': '  + '
    }
    return OPERATIONS[operation]


def get_string_line(file, key, operation):
    return f'{get_operation(operation)}{key}: {get_item(file, key)}\n'


def is_equal_item(first_file, second_file, key):
    if key in first_file and key in second_file:
        if get_item(first_file, key) == get_item(second_file, key):
            return True
    return False
