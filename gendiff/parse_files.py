from argparse import ArgumentParser


def get_parsed_data():
    parser = ArgumentParser(
        description='Compares two '
        'configuration files and shows a difference.'
    )
    parser.add_argument(
        'first_file',
        nargs='?', type=str,
        default='files/yaml/first_file.yaml'
    )
    parser.add_argument(
        'second_file',
        nargs='?', type=str,
        default='files/yaml/second_file.yaml'
    )
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    return args
