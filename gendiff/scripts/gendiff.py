from os.path import abspath
from gendiff import cli
from gendiff import generate_diff

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


def main():
    args = cli.get_args()
    abs_path_file_1 = abspath(args.first_file)
    abs_path_file_2 = abspath(args.second_file)
    formatter = get_formatter(args.format)

    print(
        generate_diff(
            abs_path_file_1,
            abs_path_file_2,
            formatter
        )
    )


if __name__ == '__main__':
    main()
