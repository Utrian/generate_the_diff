from gendiff import gendiff
from tests.fixtures import opened_json_file
from tests.fixtures import diff


def test_get_files(opened_json_file):
    result = gendiff.get_files()
    assert result == opened_json_file


def test_get_first_file(opened_json_file):
    result = gendiff.get_first_file()
    assert result == opened_json_file[0]


def test_get_second_file(opened_json_file):
    result = gendiff.get_second_file()
    assert result == opened_json_file[1]


def test_normalize_bool():
    assert gendiff.normalize_bool(0) == 0
    assert gendiff.normalize_bool(50) == 50
    assert gendiff.normalize_bool([]) == []
    assert gendiff.normalize_bool(True) == 'true'
    assert gendiff.normalize_bool(False) == 'false'
    assert gendiff.normalize_bool('sa df') == 'sa df'


def test_get_item(opened_json_file):
    assert gendiff.get_item(opened_json_file[0], 'host') == 'hexlet.io'
    assert gendiff.get_item(opened_json_file[1], 'timeout') == 20


def test_is_equal_item(opened_json_file):
    first_file, second_file = opened_json_file
    assert gendiff.is_equal_item(first_file, second_file, 'host') is True
    assert gendiff.is_equal_item(first_file, second_file, 'proxy') is False
    assert gendiff.is_equal_item(first_file, second_file, 1) is False


def test_get_string_line(opened_json_file):
    first_file, second_file = opened_json_file
    case_1 = '    host: hexlet.io\n'
    case_2 = '  - follow: false\n'
    case_3 = '  + timeout: 20\n'
    assert gendiff.get_string_line(first_file, 'host', 'Equal') == case_1
    assert gendiff.get_string_line(first_file, 'follow', 'Delete') == case_2
    assert gendiff.get_string_line(second_file, 'timeout', 'Adding') == case_3


def test_generate_diff(diff):
    assert gendiff.generate_diff() == diff
