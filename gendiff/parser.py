from os.path import abspath
from json import load as json_load
from yaml import load as yaml_load, Loader as yaml_Loader
import gendiff.formatters.stylish as ft_stylish
import gendiff.formatters.plain as ft_plain
import gendiff.formatters.json as ft_json


def get_formatter(ft_name: str):
    ft = {
        'stylish': ft_stylish.stylish,
        'plain': ft_plain.plain,
        'json': ft_json.diff_to_json
    }

    return ft[ft_name]


def get_parsed_data(args) -> tuple:
    formatter_name = get_formatter(args.format)

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

    return first_file, second_file, formatter_name
