from pytest import fixture
from gendiff import gen_diff


@fixture
def formatted_diff():
    return open('tests/fixtures/output/formatted_diff.txt').read()


@fixture
def unformatted_diff():
    return open('tests/fixtures/output/unformatted_diff.txt').read()


@fixture
def path_output_test_file():
    return 'tests/fixtures/output/output_test.txt'


@fixture
def output_test_file(path_output_test_file):
    return open(path_output_test_file).read()


def test_generate_diff(unformatted_diff):
    result = gen_diff.generate_diff()
    assert str(result) == unformatted_diff
