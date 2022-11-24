from engine import parse_files
from engine import tools
from engine import gendiff


def main():
    args = parse_files.get_parsed_data()
    first_file, second_file = tools.get_files(args)
    gendiff.generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()
