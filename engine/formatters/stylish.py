from engine.tools import (
                            normalize_bool,
                            is_nested_structure
)


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

    with open(path_output, 'r') as f:
        return f.read()
