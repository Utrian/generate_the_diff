import json
import yaml
from pytest import fixture
from gendiff import tools
from gendiff import file_parser


@fixture
def json_first_file():
    return json.load(open(tools.get_fixture_file_path('json', 'arf_file1.json')))


@fixture
def json_second_file():
    return json.load(open(tools.get_fixture_file_path('json', 'arf_file2.json')))


@fixture
def yaml_first_file():
    file_path = tools.get_fixture_file_path('yaml', 'arf_file1.yml')
    return yaml.load(open(file_path), Loader=yaml.Loader)


@fixture
def yaml_second_file():
    file_path = tools.get_fixture_file_path('yaml', 'arf_file2.yml')
    return yaml.load(open(file_path), Loader=yaml.Loader)


def test_get_parsed_data(
    json_first_file, json_second_file,
    yaml_first_file, yaml_second_file
):
    json1_path = tools.get_fixture_file_path('json', 'arf_file1.json')
    json2_path = tools.get_fixture_file_path('json', 'arf_file2.json')
    yaml1_path = tools.get_fixture_file_path('yaml', 'arf_file1.yml')
    yaml2_path = tools.get_fixture_file_path('yaml', 'arf_file2.yml')

    json_result = (
        file_parser.get_parsed_data(json1_path),
        file_parser.get_parsed_data(json2_path)
    )
    yaml_result = (
        file_parser.get_parsed_data(yaml1_path),
        file_parser.get_parsed_data(yaml2_path)
    )

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
    assert tools.normalize_bool(0) == 0
