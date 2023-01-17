import os.path
from typing import Union


def get_value(items: dict, key: str):
    value = items[key]

    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'

    elif value is None:
        return 'null'

    return value


def get_normolize_value(value):
    if isinstance(value, dict):
        return '[complex value]'

    elif value in ('true', 'false', 'null', 0):
        return value

    return f"'{value}'"


def make_message(ancestry, type, value: Union[any, list]):
    ancestry = ".".join(ancestry.split("/"))
    common_part = f"Property '{ancestry}' was"

    if type == 'changed':
        value1, value2 = value
        value1 = get_normolize_value(value1)
        value2 = get_normolize_value(value2)
        message = f'{common_part} updated. From {value1} to {value2}'
        return message

    value = get_normolize_value(value)

    if type == 'added':
        message = f'{common_part} added with value: {value}'
        return message

    elif type == 'deleted':
        message = f'{common_part} removed'
        return message


def plain(tree: list):
    diff = tree['children']
    formatted_diff = []

    def walk(diff, ancestry):
        for internal_view in diff:

            type = get_value(internal_view, 'type')
            key = get_value(internal_view, 'key')
            cur_ancestry = os.path.join(ancestry, key)

            if type == 'nested':
                children = get_value(internal_view, 'children')
                walk(children, cur_ancestry)

            elif type == 'changed':
                values = [
                    get_value(internal_view, 'value1'),
                    get_value(internal_view, 'value2')
                ]

                formatted_diff.append(
                    make_message(cur_ancestry, type, values)
                )

            elif type in ('added', 'deleted'):
                value = get_value(internal_view, 'value')
                formatted_diff.append(
                    make_message(cur_ancestry, type, value)
                )

    walk(diff, '')

    result = '\n'.join(formatted_diff)

    return result
