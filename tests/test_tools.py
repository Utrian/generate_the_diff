from pytest import fixture
from json import load as json_load
from yaml import load as yaml_load, Loader as yaml_Loader
from gendiff import tools
from gendiff import file_parser
import gendiff.formatters.plain as ft_plain


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
def json_args():
    class args:
        first_file = 'files/json/first_file.json'
        second_file = 'files/json/second_file.json'
        format = 'plain'

    return args


@fixture
def yaml_args():
    class args:
        first_file = 'files/yaml/first_file.yaml'
        second_file = 'files/yaml/second_file.yaml'
        format = 'plain'

    return args


def test_get_parsed_data(
    json_args,
    yaml_args,
    json_first_file,
    json_second_file,
    yaml_first_file,
    yaml_second_file,

):
    json_result = file_parser.get_parsed_data(json_args)
    yaml_result = file_parser.get_parsed_data(yaml_args)
    assert json_result == (json_first_file, json_second_file, ft_plain.plain)
    assert yaml_result == (yaml_first_file, yaml_second_file, ft_plain.plain)


def test_normalize_bool():
    assert tools.normalize_bool(0) == 0
    assert tools.normalize_bool(50) == 50
    assert tools.normalize_bool([]) == []
    assert tools.normalize_bool(True) == 'true'
    assert tools.normalize_bool(False) == 'false'
    assert tools.normalize_bool('sa df') == 'sa df'
    assert tools.normalize_bool(None) == 'null'
