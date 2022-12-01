from gendiff import file_parser
from gendiff import gendiff_engine
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


def generate_diff(path_file1, path_file2, formatter_name):
    formatter = get_formatter(formatter_name)
    file_1, file_2 = file_parser.get_parsed_data(path_file1, path_file2)

    diff = gendiff_engine.build_diff(file_1, file_2)

    return formatter(diff)
