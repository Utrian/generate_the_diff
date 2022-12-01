from os.path import abspath
from gendiff import cli
from gendiff import generate_diff


def main():
    args = cli.get_args()
    abs_path_file_1 = abspath(args.first_file)
    abs_path_file_2 = abspath(args.second_file)
    formatter = args.format

    print(
        generate_diff(
            abs_path_file_1,
            abs_path_file_2,
            formatter
        )
    )


if __name__ == '__main__':
    main()
