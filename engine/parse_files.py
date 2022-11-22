from argparse import ArgumentParser


def get_parsed_data():
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
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(args)
    return args
