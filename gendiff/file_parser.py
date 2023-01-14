import json
import yaml


def parser(data, format: str):
    if format in ('json', 'yaml', 'yml'):
        if format == 'json':
            parsed_data = json.load(data)
            return parsed_data

        elif format in ('yaml', 'yml'):
            parsed_data = yaml.safe_load(data)
            return parsed_data if parsed_data is not None else {}

    raise TypeError(
        f'The file extension (.{format}) is not supported.\n\n'
        'Make sure that the selected files have'
        'the extension: json, yaml or yml.'
    )


def get_data(path_file: str):
    format = path_file.split('.')[1]

    with open(path_file) as f:
        return parser(f, format)
