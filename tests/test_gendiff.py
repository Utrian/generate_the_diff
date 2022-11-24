from pytest import fixture
from json import load as json_load
from yaml import load as yaml_load, Loader as yaml_Loader
from engine import gendiff
import engine.formatters.stylish as ft_stylish


@fixture
def json_first_file():
    return json_load(open(
        'tests/fixtures/json/first_file.json')
    )


@fixture
def json_second_file():
    return json_load(open(
        'tests/fixtures/json/second_file.json')
    )


@fixture
def yaml_first_file():
    return yaml_load(open(
        'tests/fixtures/yaml/first_file.yaml'),
        Loader=yaml_Loader
    )


@fixture
def yaml_second_file():
    return yaml_load(open(
        'tests/fixtures/yaml/second_file.yaml'),
        Loader=yaml_Loader
    )


@fixture
def formatted_diff():
    with open('tests/fixtures/output/formatted_diff.txt') as f:
        return f.read()


@fixture
def unformatted_diff():
    with open('tests/fixtures/output/unformatted_diff.txt') as f:
        return f.read()


@fixture
def path_output_test_file():
    return 'tests/fixtures/output/result_test_output.txt'


@fixture
def output_test_file():
    with open('tests/fixtures/output/result_test_output.txt') as f:
        return f.read()


def test_generate_diff_json(
                        json_first_file,
                        json_second_file,
                        unformatted_diff
):
    result_with_json = gendiff.generate_diff(
        json_first_file, json_second_file
    )

    assert str(result_with_json) == unformatted_diff


def test_generate_diff_jaml(
                        yaml_first_file,
                        yaml_second_file,
                        unformatted_diff
):
    result_with_yaml = gendiff.generate_diff(
        yaml_first_file, yaml_second_file
    )

    assert str(result_with_yaml) == unformatted_diff


def test_stylish_json(
                        json_first_file,
                        json_second_file,
                        path_output_test_file,
                        output_test_file,
                        formatted_diff
):
    unf_diff_json = gendiff.generate_diff(
        json_first_file, json_second_file
    )

    ft_stylish.stylish(unf_diff_json, path_output_test_file)

    assert output_test_file == formatted_diff


def test_stylish_yaml(
                        yaml_first_file,
                        yaml_second_file,
                        path_output_test_file,
                        output_test_file,
                        formatted_diff
):
    unf_diff_yaml = gendiff.generate_diff(
        yaml_first_file, yaml_second_file
    )

    ft_stylish.stylish(unf_diff_yaml, path_output_test_file)

    assert output_test_file == formatted_diff
