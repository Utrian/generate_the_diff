import pytest
import json
from gendiff import gendiff


def test_get_files(files):
    result = gendiff.get_files()
    assert result == files


def test_normalize_bool():
    assert gendiff.normalize_bool(True) == 'true'
    assert gendiff.normalize_bool(False) == 'false'
    assert gendiff.normalize_bool(50) == 50
    assert gendiff.normalize_bool('sa df')