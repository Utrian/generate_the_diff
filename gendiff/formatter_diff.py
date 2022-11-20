from gendiff.tools import (
                            get_value,
                            get_operation,
                            is_inner_node,
                            is_changed_value
)


def stylish(diff, path_output='files/output.txt'):
    output = open(path_output, 'w')
    output.write('{\n')

    def walk(diff):
        for node in diff:
            depth = get_value(node, 'depth') - 1
            space = "    " * depth
            operation = get_operation(get_value(node, 'status'))
            key = get_value(node, 'key')
            value = get_value(node, 'value')

            if is_inner_node(value):
                indent = ' ' * len(space + operation)
                open_bracket = '{'
                close_bracket = f"{indent}{'}'}"

                output.write(f"{space}{operation}{key}: {open_bracket}\n")
                walk(value)
                output.write(f"{close_bracket}\n")
                continue

            elif is_changed_value(value):
                operation_1, operation_2 = operation
                value_1, value_2 = value
                output.write(f"{space}{operation_1}{key}: {value_1}\n")
                output.write(f"{space}{operation_2}{key}: {value_2}\n")
                continue

            output.write(f"{space}{operation}{key}: {value}\n")

    walk(diff)
    output.write('}')
    output.close()
