import json
import os.path
import argparse
from collections import Counter


OPERATIONS = {
    'Equal': '    ',
    'Delete': '  - ',
    'Adding': '  + '
}


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

    args = parser.parse_args(['files/first_file.json', 'files/second_file.json'])

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


def is_equal_item(first_file, second_file, key):
    if key in first_file and key in second_file:
        if get_item(first_file, key) == get_item(second_file, key):
            return True
    return False


def get_string_line(file, key, operation):
    return f'{OPERATIONS[operation]}{key}: {get_item(file, key)}'


def generate_diff():
    first_file, second_file = get_files()
    all_keys = sorted(
        [key for key in first_file] + [key for key in second_file]
    )
    parameter_counter = Counter(all_keys)

    parameters = ['{']

    for key, value in parameter_counter.items():

        if value == 2:
            if is_equal_item(first_file, second_file, key):
                parameters.append((
                    get_string_line(first_file, key, 'Equal')
                ))
                continue
            parameters.append(get_string_line(first_file, key, 'Delete'))
            parameters.append(get_string_line(second_file, key, 'Adding'))

        elif key in first_file:
            parameters.append(get_string_line(first_file, key, 'Delete'))

        else:
            parameters.append(get_string_line(second_file, key, 'Adding'))

    parameters.append('}')

    final_diff = '\n'.join(parameters)

    print(final_diff)

    return final_diff

    # with open('files/output.txt', 'w') as output:
    #     for key, value in parameter_counter.items():

    #         if value == 2:
    #             if is_equal_item(first_file, second_file, key):
    #                 output.write(get_equal_item(key))
    #                 continue
    #             output.write(get_item_from_first_file(key))
    #             output.write(get_item_from_second_file(key))

    #         elif key in first_file:
    #             output.write(get_item_from_first_file(key))

    #         else:
    #             output.write(get_item_from_second_file(key))

    #     output.write('}')
