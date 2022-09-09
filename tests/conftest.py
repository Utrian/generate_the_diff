import pytest
import json


@pytest.fixture
def files():
    first_file = json.load(open('files/first_file.json'))
    second_file = json.load(open('files/second_file.json'))
    return first_file, second_file