from json import load as json_load, JSONDecodeError
from yaml import load as yaml_load, Loader as yaml_Loader


def get_data(path_file, format):
    if format in ('json', 'yaml', 'yml'):
        if format == 'json':
            try:
                parsed_data = json_load(open(path_file))
                return parsed_data

            except JSONDecodeError:
                return {}

        elif format in ('yaml', 'yml'):
            parsed_data = yaml_load(open(path_file), Loader=yaml_Loader)
            return parsed_data if parsed_data is not None else {}


def get_parsed_data(path_file1, path_file2) -> tuple:

    first_file_format = path_file1.split('.')[1]
    second_file_format = path_file2.split('.')[1]

    first_file = get_data(path_file1, first_file_format)
    second_file = get_data(path_file2, second_file_format)

    return first_file, second_file
