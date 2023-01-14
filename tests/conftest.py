import os


def get_fixture_file_path(format, file_name):
    file_path = os.path.abspath(os.path.join('tests', 'fixtures', format, file_name))
    return file_path
