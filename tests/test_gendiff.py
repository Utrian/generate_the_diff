from pytest import fixture
from json import load as json_load
from yaml import load as yaml_load, Loader as yaml_Loader
from gendiff import tools
from gendiff import gendiff


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
def diff():
    return open('tests/fixtures/diff.txt').read()


def test_get_files(
        json_first_file,
        json_second_file,
        yaml_first_file,
        yaml_second_file
        ):
    result = tools.get_files()
    assert result == (json_first_file, json_second_file)
    assert result == (yaml_first_file, yaml_second_file)


def test_get_first_file(json_first_file, yaml_first_file):
    result = tools.get_first_file()
    assert result == json_first_file
    assert result == yaml_first_file


def test_get_second_file(json_second_file, yaml_second_file):
    result = tools.get_second_file()
    assert result == json_second_file
    assert result == yaml_second_file


def test_normalize_bool():
    assert tools.normalize_bool(0) == 0
    assert tools.normalize_bool(50) == 50
    assert tools.normalize_bool([]) == []
    assert tools.normalize_bool(True) == 'true'
    assert tools.normalize_bool(False) == 'false'
    assert tools.normalize_bool('sa df') == 'sa df'


def test_generate_diff(diff):
    assert gendiff.generate_diff() == diff
