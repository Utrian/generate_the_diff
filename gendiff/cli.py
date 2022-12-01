from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser(
        description='Compares two '
        'configuration files and shows a difference.'
    )
    parser.add_argument(
        'first_file',
        nargs='?', type=str,
        default='files/json/first_file.json'
    )
    parser.add_argument(
        'second_file',
        nargs='?', type=str,
        default='files/json/second_file.json'
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
