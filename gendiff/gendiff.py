import argparse
import os.path
import json
from collections import Counter


def parser():
    parser = argparse.ArgumentParser(
        description='Compares two '
        'configuration files and shows a difference.'
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    return args


def get_files() -> dict:
    args = parser()

    abs_path_first_file = os.path.abspath(args.first_file)
    abs_path_second_file = os.path.abspath(args.second_file)

    first_file = json.load(open(abs_path_first_file))
    second_file = json.load(open(abs_path_second_file))

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


def print_equal_item(first_file, second_file, key):
    if key in first_file and key in second_file:
        if get_item(first_file, key) == get_item(second_file, key):
            print(f'     {key}: {get_item(first_file, key)}')
            return True


def print_item_from_first_file(key):
    first_file = get_first_file()
    print(f'  -  {key}: {get_item(first_file, key)}')


def print_item_from_second_file(key):
    second_file = get_second_file()
    print(f'  +  {key}: {get_item(second_file, key)}')


def generate_diff():
    first_file, second_file = get_files()
    all_keys = sorted(
        [key for key in first_file] + [key for key in second_file]
    )
    parameter_counter = Counter(all_keys)

    print('{')
    for key, value in parameter_counter.items():

        if value == 2:
            if print_equal_item(first_file, second_file, key):
                continue
            print_item_from_first_file(key)
            print_item_from_second_file(key)

        elif key in first_file:
            print_item_from_first_file(key)

        else:
            print_item_from_second_file(key)
    print('}')
