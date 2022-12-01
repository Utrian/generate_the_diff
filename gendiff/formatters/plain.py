import os.path
from typing import Union
from gendiff.tools import (get_value, normalize_bool)


def write_message(output_file, ancestry, type, value: Union[any, list]):
    ancestry = ".".join(ancestry.split("/"))
    common_part = f"Property '{ancestry}' was"

    if type == 'changed':
        value1, value2 = value
        value1 = normalize_bool(value1, 'plain')
        value2 = normalize_bool(value2, 'plain')

        message = f'{common_part} updated. From {value1} to {value2}\n'
        output_file.write(message)
        return

    value = normalize_bool(value, 'plain')

    if type == 'added':
        message = f'{common_part} added with value: {value}\n'
        output_file.write(message)

    elif type == 'deleted':
        message = f'{common_part} removed\n'
        output_file.write(message)


def plain(diff: list, path_output='files/output.txt'):
    output = open(path_output, 'w')

    def walk(diff, ancestry):
        for internal_view in diff:

            type = get_value(internal_view, 'type')
            key = get_value(internal_view, 'key')
            cur_ancestry = os.path.join(ancestry, key)

            if type == 'nested':
                children = get_value(internal_view, 'children')
                walk(children, cur_ancestry)

            elif type == 'changed':
                values = []

                if 'value1' in internal_view:
                    values.append(get_value(internal_view, 'value1'))

                if 'children' in internal_view:
                    values.append(get_value(internal_view, 'children'))

                if 'value2' in internal_view:
                    values.append(get_value(internal_view, 'value2'))

                write_message(output, cur_ancestry, type, values)

            elif type in ('added', 'deleted'):
                if 'value' in internal_view:
                    value = get_value(internal_view, 'value')

                elif 'children' in internal_view:
                    value = get_value(internal_view, 'children')

                write_message(output, cur_ancestry, type, value)

    walk(diff, '')
    output.close()

    with open(path_output, 'r') as f:
        return f.read()
