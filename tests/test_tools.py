from pytest import fixture
from json import load as json_load
from yaml import load as yaml_load, Loader as yaml_Loader
from engine import tools


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
        format = None

    return args


@fixture
def yaml_args():
    class args:
        first_file = 'files/yaml/first_file.yaml'
        second_file = 'files/yaml/second_file.yaml'
        format = None

    return args


def test_get_files(
    json_args,
    yaml_args,
    json_first_file,
    json_second_file,
    yaml_first_file,
    yaml_second_file
):
    json_result = tools.get_files(json_args)
    yaml_result = tools.get_files(yaml_args)
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
