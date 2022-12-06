import json
import yaml


def get_parsed_data(path_file):
    file_format = path_file.split('.')[1]

    if file_format in ('json', 'yaml', 'yml'):
        if file_format == 'json':
            parsed_data = json.load(open(path_file))
            return parsed_data

        elif file_format in ('yaml', 'yml'):
            parsed_data = yaml.safe_load(open(path_file))
            return parsed_data if parsed_data is not None else {}

    raise TypeError(
        f'The file extension (.{file_format}) is not supported.\n\n'
        'Make sure that the selected files have'
        'the extension: json, yaml or yml.'
    )
