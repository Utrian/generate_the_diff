import os.path
from typing import Union
from gendiff.tools import is_nested_structure


def make_message(ancestry, status, value: Union[any, tuple]) -> str:
    ancestry = ".".join(ancestry.split("/"))
    common_part = f"Property '{ancestry}' was"

    if status == "updated":
        pre_value, new_value = value
        return f"{common_part} updated. From {pre_value} to {new_value}\n"

    if status == "+":
        return f"{common_part} added with value: {value}\n"

    if status == "-":
        return f"{common_part} removed\n"


def is_changed(pre_key: str, diff: dict):
    wanted_key = f'  + {pre_key}'

    if wanted_key in diff:
        next_value = diff.get(wanted_key)

        if is_nested_structure(next_value):
            return '[complex value]'

        return normalize_value(next_value)

    return False


def normalize_value(value):
    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'

    if value is None:
        return 'null'

    return f"'{value}'"


def plain(diff: dict, path_output='files/output.txt'):
    output = open(path_output, 'w')

    def walk(diff, pre_ancestry, jump=False):
        for key, value in diff.items():

            if jump is True:
                jump = False
                continue

            status = key[2]
            name_key = key[4:]
            message_value = normalize_value(value)
            ancestry = os.path.join(pre_ancestry, name_key)

            if is_nested_structure(value):
                message_value = "[complex value]"

                if status == ' ':
                    walk(value, ancestry)

            if status == '+':
                message = make_message(
                                        ancestry, status,
                                        message_value
                )
                output.write(message)

            elif status == '-':
                next_value_is_changed = is_changed(name_key, diff)

                if next_value_is_changed is False:
                    message = make_message(
                                            ancestry, status,
                                            message_value
                    )
                    output.write(message)

                else:
                    jump = True

                    next_value = next_value_is_changed
                    values = (message_value, next_value)

                    message = make_message(ancestry, 'updated', values)
                    output.write(message)

    walk(diff, '')
    output.close()

    with open(path_output, 'r') as f:
        return f.read()
