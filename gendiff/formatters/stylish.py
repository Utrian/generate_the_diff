from gendiff.tools import (
                            get_value,
                            get_status,
                            normalize_bool
)


def write_line(output_file, indent, type, key, value):
    value = normalize_bool(value)
    visual_type = get_status(type)

    output_file.write(f"{indent}{visual_type}{key}: {value}\n")


def write_close_bracket(output_file, indent='', default_indent=0):
    closing_bracket_indent = ' ' * (len(indent) + default_indent)
    close_bracket = f"{closing_bracket_indent}{'}'}"

    output_file.write(f"{close_bracket}\n")


def stylish(diff: list, path_output='files/output.txt'):
    spaces = "    "
    open_bracket = '{'
    default_indent = 4

    output = open(path_output, 'w')
    output.write('{\n')

    def walk(diff, depth=0):
        for internal_view in diff:
            key = get_value(internal_view, 'key')
            type = get_value(internal_view, 'type')
            indent = spaces * depth

            if 'value' in internal_view:
                value = get_value(internal_view, 'value')
                write_line(output, indent, type, key, value)

            elif 'children' in internal_view and type != 'changed':
                children = get_value(internal_view, 'children')

                write_line(output, indent, type, key, open_bracket)
                walk(children, depth + 1)
                write_close_bracket(output, indent, default_indent)

                continue

            type1 = 'deleted'
            type2 = 'added'

            if 'value1' in internal_view:
                value1 = get_value(internal_view, 'value1')
                write_line(output, indent, type1, key, value1)

            if 'children' in internal_view:
                child_type = type1

                if 'value1' in internal_view:
                    child_type = type2
                
                children = get_value(internal_view, 'children')
                closing_bracket_indent = ' ' * (len(indent) + default_indent)
                close_bracket = f"{closing_bracket_indent}{'}'}"
                
                write_line(output, indent, child_type, key, open_bracket)
                walk(children, depth + 1)
                output.write(f"{close_bracket}\n")
            
            if 'value2' in internal_view:
                value2 = get_value(internal_view, 'value2')

                write_line(output, indent, type2, key, value2)

    walk(diff)

    write_close_bracket(output)
    output.close()

    with open(path_output, 'r') as f:
        return f.read()
