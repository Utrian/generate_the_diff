from json import load as json_load
from yaml import load as yaml_load, Loader as yaml_Loader


def get_parsed_data(path_file1, path_file2) -> tuple:

    first_file_format = path_file1.split('.')[1]
    second_file_format = path_file2.split('.')[1]

    if first_file_format == 'json':
        first_file = json_load(open(path_file1))

    elif first_file_format in ['yml', 'yaml']:
        first_file = yaml_load(open(path_file1), Loader=yaml_Loader)

    if second_file_format == 'json':
        second_file = json_load(open(path_file2))

    elif second_file_format in ['yml', 'yaml']:
        second_file = yaml_load(open(path_file2), Loader=yaml_Loader)

    return first_file, second_file
