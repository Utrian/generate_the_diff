SPACES = "    "
OPEN_BRACKET = '{'
DEFAULT_INDENT = 4


def get_normalize_value(items: dict, key: str):
    value = items[key]

    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'

    elif value is None:
        return 'null'

    return value


def get_type(status: str):
    statuses = {
        'added': '  + ',
        'deleted': '  - ',
        'nested': '    ',
        'unchanged': '    '
    }
    return statuses[status]


def write_line(indent, type, key, value):
    visual_type = get_type(type)

    return f"{indent}{visual_type}{key}: {value}"


def write_close_bracket(indent):
    closing_bracket_indent = ' ' * (len(indent) + DEFAULT_INDENT)
    close_bracket = f"{closing_bracket_indent}{'}'}"

    return f"{close_bracket}"


def external_walk(dict_, depth):
    type = 'unchanged'

    lines = list()

    def walk(dict_, depth):
        keys = [key for key in dict_]

        for key in keys:
            indent = SPACES * depth

            if isinstance(dict_[key], dict):
                lines.append(write_line(indent, type, key, OPEN_BRACKET))
                walk(dict_[key], depth + 1)
                lines.append(write_close_bracket(indent))

            else:
                value = dict_[key]
                lines.append(write_line(indent, type, key, value))

        return lines
    return walk(dict_, depth)


def stylish(tree: list):
    diff = tree['children']

    formatted_diff = [OPEN_BRACKET]

    def walk(diff, depth=0):
        for internal_view in diff:
            key = internal_view['key']
            type = internal_view['type']
            indent = SPACES * depth

            if 'value' in internal_view:
                value = get_normalize_value(internal_view, 'value')

                if isinstance(value, dict):
                    children = external_walk(value, depth + 1)
                    formatted_diff.append(
                        write_line(indent, type, key, OPEN_BRACKET)
                    )
                    formatted_diff.extend(children)
                    formatted_diff.append(write_close_bracket(indent))
                else:
                    formatted_diff.append(
                        write_line(indent, type, key, value)
                    )

                continue

            elif 'children' in internal_view:
                children = internal_view['children']

                formatted_diff.append(
                    write_line(indent, type, key, OPEN_BRACKET)
                )
                walk(children, depth + 1)
                formatted_diff.append(write_close_bracket(indent))

                continue

            value1 = get_normalize_value(internal_view, 'value1')
            value2 = get_normalize_value(internal_view, 'value2')

            types_with_values = zip(
                ('deleted', 'added'),
                (value1, value2)
            )

            for type_and_value in types_with_values:
                type, value = type_and_value

                if isinstance(value, dict):
                    children = external_walk(value, depth + 1)

                    formatted_diff.append(
                        write_line(indent, type, key, OPEN_BRACKET)
                    )
                    formatted_diff.extend(children)
                    formatted_diff.append(write_close_bracket(indent))

                else:
                    formatted_diff.append(
                        write_line(indent, type, key, value)
                    )
    walk(diff)

    formatted_diff.append('}')

    result = '\n'.join(formatted_diff)
    return result
