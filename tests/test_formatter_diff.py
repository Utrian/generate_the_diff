# from pytest import fixture
# from gendiff.formatter_diff import stylish


# @fixture
# def formatted_diff():
#     return open('tests/fixtures/output/formatted_diff.txt').read()


# @fixture
# def unformatted_diff():
#     return list(open('tests/fixtures/output/unformatted_diff.txt'))


# @fixture
# def path_output_test_file():
#     return 'tests/fixtures/output/output_test.txt'


# @fixture
# def output_test_file(path_output_test_file):
#     return open(path_output_test_file).read()


# def test_generate_diff(
#         unformatted_diff,
#         formatted_diff,
#         path_output_test_file,
#         output_test_file
# ):
#     stylish(unformatted_diff, path_output_test_file)
#     result = output_test_file
#     assert result == formatted_diff
