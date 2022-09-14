import pytest


@pytest.fixture
def opened_json_file():
    return ({
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
        },
        {
        'timeout': 20,
        'verbose': True,
        'host': 'hexlet.io'
        }
    )


@pytest.fixture
def diff():
    return '\n'.join([
        '{',
        '  -  follow: false',
        '     host: hexlet.io',
        '  -  proxy: 123.234.53.22',
        '  -  timeout: 50', '  +  timeout: 20',
        '  +  verbose: true',
        '}'
    ])
