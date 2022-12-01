from gendiff.tools import get_value, get_status


def write_line(indent, type, key, value):
    visual_type = get_status(type)

    return f"{indent}{visual_type}{key}: {value}"


def write_close_bracket(indent='', default_indent=0):
    closing_bracket_indent = ' ' * (len(indent) + default_indent)
    close_bracket = f"{closing_bracket_indent}{'}'}"

    return f"{close_bracket}"


def stylish(diff: list):
    spaces = "    "
    open_bracket = '{'
    default_indent = 4

    formatted_diff = [open_bracket]

    def walk(diff, depth=0):
        for internal_view in diff:
            key = get_value(internal_view, 'key')
            type = get_value(internal_view, 'type')
            indent = spaces * depth

            if 'value' in internal_view:
                value = get_value(internal_view, 'value')
                formatted_diff.append(write_line(indent, type, key, value))

            elif 'children' in internal_view and type != 'changed':
                children = get_value(internal_view, 'children')

                formatted_diff.append(write_line(indent, type, key, open_bracket))
                walk(children, depth + 1)
                formatted_diff.append(
                    write_close_bracket(indent, default_indent)
                )

                continue

            type1 = 'deleted'
            type2 = 'added'

            if 'value1' in internal_view:
                value1 = get_value(internal_view, 'value1')
                formatted_diff.append(write_line(indent, type1, key, value1))

            if 'children' in internal_view:
                child_type = type1

                if 'value1' in internal_view:
                    child_type = type2

                children = get_value(internal_view, 'children')
                closing_bracket_indent = ' ' * (len(indent) + default_indent)
                close_bracket = f"{closing_bracket_indent}{'}'}"

                formatted_diff.append(
                    write_line(indent, child_type, key, open_bracket)
                )
                walk(children, depth + 1)
                formatted_diff.append(f"{close_bracket}")

            if 'value2' in internal_view:
                value2 = get_value(internal_view, 'value2')

                formatted_diff.append(write_line(indent, type2, key, value2))

    walk(diff)

    formatted_diff.append(write_close_bracket())

    result = '\n'.join(formatted_diff)
    return result
