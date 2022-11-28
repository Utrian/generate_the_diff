from pytest import fixture
from json import load as json_load
from yaml import load as yaml_load, Loader as yaml_Loader
from engine import gendiff
import engine.formatters.stylish as ft_stylish
import engine.formatters.plain as ft_plain
import engine.formatters.json as ft_json


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
def path_output_test_file():
    return 'tests/output.txt'


@fixture
def result_output():
    with open('tests/output.txt') as f:
        return f.read()


@fixture
def unformatted_diff():
    with open('tests/fixtures/output/unformatted_diff.txt') as f:
        return f.read()


@fixture
def stylish_formatted_diff():
    with open('tests/fixtures/output/stylish_formatted_diff.txt') as f:
        return f.read()


@fixture
def plain_formatted_diff():
    with open('tests/fixtures/output/plain_formatted_diff.txt') as f:
        return f.read()


@fixture
def json_formatted_diff():
    with open('tests/fixtures/output/json_formatted_diff.txt') as f:
        return f.read()


def test_generate_diff_json(
                        json_first_file,
                        json_second_file,
                        unformatted_diff
):
    unformatted_diff_json = gendiff.generate_diff(
        json_first_file, json_second_file
    )[0]

    assert str(unformatted_diff_json) == unformatted_diff


def test_generate_diff_jaml(
                        yaml_first_file,
                        yaml_second_file,
                        unformatted_diff
):
    unformatted_diff_yaml = gendiff.generate_diff(
        yaml_first_file, yaml_second_file
    )[0]

    assert str(unformatted_diff_yaml) == unformatted_diff


def test_stylish_json(
                        json_first_file,
                        json_second_file,
                        stylish_formatted_diff,
):
    result_formatted_diff = gendiff.generate_diff(
        json_first_file, json_second_file, ft_stylish.stylish
    )[1]

    assert result_formatted_diff == stylish_formatted_diff


def test_stylish_yaml(
                        yaml_first_file,
                        yaml_second_file,
                        stylish_formatted_diff
):
    result_formatted_diff = gendiff.generate_diff(
        yaml_first_file, yaml_second_file, ft_stylish.stylish
    )[1]

    assert result_formatted_diff == stylish_formatted_diff


def test_plain_json(
                    json_first_file,
                    json_second_file,
                    plain_formatted_diff
):
    formatted_diff_json = gendiff.generate_diff(
        json_first_file, json_second_file, ft_plain.plain
    )[1]

    assert formatted_diff_json == plain_formatted_diff


def test_plain_yaml(
                    yaml_first_file,
                    yaml_second_file,
                    plain_formatted_diff
):
    formatted_diff_yaml = gendiff.generate_diff(
        yaml_first_file, yaml_second_file, ft_plain.plain
    )[1]

    assert formatted_diff_yaml == plain_formatted_diff


def test_diff_to_json_with_json_file(
                                    json_first_file,
                                    json_second_file,
                                    json_formatted_diff
):
    formatted_diff_json = gendiff.generate_diff(
        json_first_file, json_second_file, ft_json.diff_to_json
    )[1]

    assert formatted_diff_json == json_formatted_diff


def test_diff_to_json_with_yaml_file(
                                    yaml_first_file,
                                    yaml_second_file,
                                    json_formatted_diff
):
    formatted_diff_yaml = gendiff.generate_diff(
        yaml_first_file, yaml_second_file, ft_json.diff_to_json
    )[1]

    assert formatted_diff_yaml == json_formatted_diff
