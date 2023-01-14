import os
from argparse import ArgumentParser


def get_fixture_file_path(format, file_name):
    file_path = os.path.abspath(os.path.join('tests', 'fixtures', format, file_name))
    return file_path


def get_args():
    file1_path = get_fixture_file_path('json', 'arf_file1.json')
    file2_path = get_fixture_file_path('json', 'arf_file2.json')

    parser = ArgumentParser(
        description='Compares two '
        'configuration files and shows a difference.'
    )
    parser.add_argument(
        'first_file',
        nargs='?', type=str,
        default=file1_path
    )
    parser.add_argument(
        'second_file',
        nargs='?', type=str,
        default=file2_path
    )
    parser.add_argument(
        '-f', '--format',
        nargs='?', type=str,
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output'
    )

    args = parser.parse_args()
    return args
