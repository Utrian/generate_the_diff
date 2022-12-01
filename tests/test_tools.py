from pytest import fixture
from json import load as json_load
from yaml import load as yaml_load, Loader as yaml_Loader
from gendiff import tools
from gendiff import file_parser


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


def test_get_parsed_data(
    json_first_file, json_second_file,
    yaml_first_file, yaml_second_file
):
    json1_path = 'tests/fixtures/json/first_file.json'
    json2_path = 'tests/fixtures/json/second_file.json'
    yaml1_path = 'tests/fixtures/yaml/first_file.yaml'
    yaml2_path = 'tests/fixtures/yaml/second_file.yaml'

    json_result = file_parser.get_parsed_data(json1_path, json2_path)
    yaml_result = file_parser.get_parsed_data(yaml1_path, yaml2_path)

    assert json_result == (json_first_file, json_second_file)
    assert yaml_result == (yaml_first_file, yaml_second_file)


def test_normalize_bool():
    assert tools.normalize_bool(0) == 0
    assert tools.normalize_bool(50) == 50
    assert tools.normalize_bool([]) == []
    assert tools.normalize_bool(True) == 'true'
    assert tools.normalize_bool(False) == 'false'
    assert tools.normalize_bool('sa df') == 'sa df'
    assert tools.normalize_bool(None) == 'null'
