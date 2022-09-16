import json
import os.path
import argparse
from collections import Counter


def parser():
    parser = argparse.ArgumentParser(
        description='Compares two '
        'configuration files and shows a difference.'
    )
    parser.add_argument(
        'first_file',
        nargs='?', type=str,
        default='files/first_file.json'
    )
    parser.add_argument(
        'second_file',
        nargs='?', type=str,
        default='files/second_file.json'
    )
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args([
        'files/first_file.json',
        'files/second_file.json'
    ])

    return args


def get_files() -> dict:
    args = parser()

    abs_path_first_file = os.path.abspath(args.first_file)
    abs_path_second_file = os.path.abspath(args.second_file)

    if (abs_path_first_file[-4:] == 'json' and
        abs_path_second_file[-4:] == 'json'):
        first_file = json.load(open(abs_path_first_file))
        second_file = json.load(open(abs_path_second_file))

    elif (abs_path_first_file[-4:] == 'yaml' and
        abs_path_second_file[-4:] == 'yaml'):
        pass


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


def generate_diff():
    first_file, second_file = get_files()
    all_keys = sorted(
        [key for key in first_file] +
        [key for key in second_file if not key in first_file]
    )

    with open('files/output.txt', 'w+') as output:
        output.write('{\n')
        for key in all_keys:
            if is_equal_item(first_file, second_file, key):
                output.write(get_string_line(first_file, key, 'Equal'))
            elif key in first_file and key in second_file:
                output.write(get_string_line(first_file, key, 'Delete'))
                output.write(get_string_line(second_file, key, 'Adding'))
            elif key in first_file:
                output.write(get_string_line(first_file, key, 'Delete'))
            elif key in second_file:
                output.write(get_string_line(second_file, key, 'Adding'))
        output.write('}')  

        output.seek(0)
        diff = output.read()
        print(diff)

    return diff