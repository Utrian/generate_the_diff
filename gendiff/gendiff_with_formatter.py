from gendiff import file_parser
from gendiff import gendiff_engine


def generate_diff(path_file1, path_file2, formatter):
    file_1, file_2 = file_parser.get_parsed_data(path_file1, path_file2)

    diff = gendiff_engine.build_diff(file_1, file_2)

    return formatter(diff)
