from gendiff import cli
from gendiff import parser
from gendiff import gendiff


def main():
    args = cli.get_args()
    first_file, second_file, formatter = parser.get_parsed_data(args)
    gendiff.generate_diff(first_file, second_file, formatter)


if __name__ == '__main__':
    main()
