from engine.tools import (
                            get_value,
                            is_nested_structure
)

def get_value(file, key):
    return file[key]


def is_nested_structure(key, *files):
    if len(files) == 2:
        first_file, second_file = files

        if key in first_file and key in second_file:
            return (
                isinstance(get_value(first_file, key), dict) and
                isinstance(get_value(second_file, key), dict)
            )
        return False

    if files == ():
        value = key
        return isinstance(value, dict)

    file = files[0]

    return isinstance(file[key], dict)


def normalize_bool(value):
    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'

    if value is None:
        return 'null'

    return value


def stylish(diff: dict, path_output='files/output.txt'):
    operation_indent = 4

    output = open(path_output, 'w')
    output.write('{\n')

    def walk(diff, depth=0):
        for key, value in diff.items():
            space = "    " * depth

            if is_nested_structure(value):
                indent = ' ' * (len(space) + operation_indent)
                open_bracket = '{'
                close_bracket = f"{indent}{'}'}"

                output.write(f"{space}{key}: {open_bracket}\n")
                walk(value, depth + 1)
                output.write(f"{close_bracket}\n")

                continue

            output.write(f"{space}{key}: {normalize_bool(value)}\n")

    walk(diff)
    output.write('}')
    output.close()
