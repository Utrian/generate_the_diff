from gendiff import file_parser
from . import diff_tree
from gendiff import data_formatting


def generate_diff(path_file1, path_file2, formatter_name='stylish'):
    data_1 = file_parser.get_data(path_file1)
    data_2 = file_parser.get_data(path_file2)

    diff = diff_tree.build_diff_tree(data_1, data_2)
    result = data_formatting.formatting(diff, formatter_name)

    return result
