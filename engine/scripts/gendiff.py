from engine import cli
from engine import parser
from engine import gendiff


def main():
    args = cli.get_args()
    first_file, second_file, formatter = parser.get_parsed_data(args)
    gendiff.generate_diff(first_file, second_file, formatter)


if __name__ == '__main__':
    main()
