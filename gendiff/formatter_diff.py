from tools import get_value, get_operation, is_inner_node, is_changed_value
from os.path import abspath
import gen_diff

PATH_OUTPUT_FILE = abspath('files/output.txt')


# def clear_output_file():
#     with open(PATH_OUTPUT_FILE, 'w'):
#         pass


# clear_output_file()


# def is_inner_node():


def stylish(diff):
    with open(PATH_OUTPUT_FILE, 'a') as output:
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

                output.write(f"{indent}{operation}{key}: {open_bracket}\n")
                stylish(value)
                output.write(f"{close_bracket}\n")
                continue

            elif is_changed_value(value):
                operation_1, operation_2 = operation
                value_1, value_2 = value
                output.write(f"{space}{operation_1}{key}: {value_1}\n")
                output.write(f"{space}{operation_2}{key}: {value_2}\n")
                continue

            output.write(f"{space}{operation}{key}: {value}\n")
    
    return 'Complete'


stylish(gen_diff.generate_diff())