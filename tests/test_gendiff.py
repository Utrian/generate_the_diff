import os
import pytest
from gendiff.gendiff_with_formatter import generate_diff


def get_path(parent, file):
    return os.path.join('tests', 'fixtures', parent, file)


@pytest.mark.parametrize(
    "fixtura_parent, test_file1, test_file2, formatter, expected",
    [
        pytest.param(
            'json',
            'arf_file1.json',
            'arf_file2.json',
            'stylish',
            'arf_result_stylish',
            id='arf stylish recursive json comparison'
        ),
        pytest.param(
            'yaml',
            'arf_file1.yml',
            'arf_file2.yml',
            'stylish',
            'arf_result_stylish',
            id='arf stylish recursive yml comparison'
        ),
        pytest.param(
            'json',
            'first_file.json',
            'second_file.json',
            'stylish',
            'stylish_formatted_diff.txt',
            id='stylish recursive json comparison'
        ),
        pytest.param(
            'yaml',
            'first_file.yaml',
            'second_file.yaml',
            'stylish',
            'stylish_formatted_diff.txt',
            id='stylish recursive yaml comparison'
        ),
        pytest.param(
            'json',
            'arf_file1.json',
            'arf_file2.json',
            'plain',
            'arf_result_plain',
            id='arf plain recursive json comparison'
        ),
        pytest.param(
            'yaml',
            'arf_file1.yml',
            'arf_file2.yml',
            'plain',
            'arf_result_plain',
            id='arf plain recursive yml comparison'
        ),
        pytest.param(
            'json',
            'first_file.json',
            'second_file.json',
            'plain',
            'plain_formatted_diff.txt',
            id='plain recursive json comparison'
        ),
        pytest.param(
            'yaml',
            'first_file.yaml',
            'second_file.yaml',
            'plain',
            'plain_formatted_diff.txt',
            id='plain recursive yaml comparison'
        ),
    ],
)
def test_generate_diff(
    fixtura_parent, test_file1,
    test_file2, formatter, expected
):
    expected_path = get_path('output', expected)
    with open(expected_path, 'r') as f:
        test_path1 = get_path(fixtura_parent, test_file1)
        test_path2 = get_path(fixtura_parent, test_file2)

        expected_result = f.read()
        function_result = generate_diff(test_path1, test_path2, formatter)
        assert function_result == expected_result


def test_generate_diff_mix_file_types():
    stylish_expected_path = get_path('output', 'arf_result_stylish')
    plain_expected_path = get_path('output', 'arf_result_plain')

    with open(stylish_expected_path, 'r') as st_file:
        test_path1 = get_path('json', 'arf_file1.json')
        test_path2 = get_path('yaml', 'arf_file2.yml')

        expected_result = st_file.read()
        function_result = generate_diff(test_path1, test_path2, 'stylish')
        assert function_result == expected_result

    with open(plain_expected_path, 'r') as pl_file:
        test_path1 = get_path('yaml', 'arf_file1.yml')
        test_path2 = get_path('json', 'arf_file2.json')

        expected_result = pl_file.read()
        function_result = generate_diff(test_path1, test_path2, 'plain')
        assert function_result == expected_result


def test_generate_diff_with_empty_file():
    stylish_expected_path = get_path(
        'output', 'stylish_empty_file_vs_arf_file2.txt'
    )
    plain_expected_path = get_path(
        'output', 'plain_empty_file_vs_arf_file2.txt'
    )

    test_path1 = get_path('yaml', 'empty_file.yml')
    test_path2 = get_path('json', 'arf_file2.json')

    with open(stylish_expected_path, 'r') as st_file:
        expected_result = st_file.read()
        function_result = generate_diff(test_path1, test_path2, 'stylish')
        assert function_result == expected_result

    with open(plain_expected_path, 'r') as pl_file:
        expected_result = pl_file.read()
        function_result = generate_diff(test_path1, test_path2, 'plain')
        assert function_result == expected_result
