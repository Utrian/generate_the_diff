# import engine.formatters.stylish as ft_stylish
# import engine.formatters.json as ft_json
import engine.formatters.plain as ft_plain
from engine.tools import (
                            get_value, is_equal_items,
                            is_nested_structure, get_status
)

def formatter():
    def wrapper(format):
        return format()

def external_walk(file):
    diff = dict()
    all_keys = list([key for key in file])

    for key in all_keys:
        if is_nested_structure(key, file):
            child = external_walk(get_value(file, key))
            diff[get_status('equal') + key] = child
            continue

        diff[get_status('equal') + key] = get_value(file, key)

    return diff


def generate_diff(
                file_1,
                file_2,
                format_name=ft_plain.plain
):

    def walk(file_1, file_2):
        diff = dict()
        all_keys = sorted(list(
            [key for key in file_1] +
            [key for key in file_2 if key not in file_1]
        ))

        for key in all_keys:

            if is_nested_structure(key, file_1, file_2):
                child = walk(
                    get_value(file_1, key),
                    get_value(file_2, key)
                )

                diff[get_status('equal') + key] = child

            elif is_equal_items(file_1, file_2, key):
                diff[get_status('equal') + key] = get_value(file_1, key)

            else:
                if key in file_1:
                    if is_nested_structure(key, file_1):
                        child = external_walk(
                            get_value(file_1, key)
                        )

                        diff[get_status('deleted') + key] = child

                    else:
                        value = get_value(file_1, key)
                        diff[get_status('deleted') + key] = value

                if key in file_2:
                    if is_nested_structure(key, file_2):
                        child = external_walk(
                            get_value(file_2, key)
                        )

                        diff[get_status('added') + key] = child

                    else:
                        value = get_value(file_2, key)
                        diff[get_status('added') + key] = value

        return diff

    unformatted_diff = walk(file_1, file_2)
    print(format_name(unformatted_diff))

    return unformatted_diff