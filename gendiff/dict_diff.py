from gendiff.tools import get_files, get_first_file, get_second_file, is_equal_items, is_inner_node, is_inner_nodes, is_not_equal_items


def generate_diff(first_file=get_first_file(), second_file=get_second_file()):
    # if first_file is None and second_file is None:
    #     first_file, second_file = get_files()

    diff = list()
    all_keys = sorted(list(
        set(first_file.keys()) | set(second_file.keys())
    ))

    for key in all_keys:
        if is_inner_nodes(first_file, second_file, key):
            child = generate_diff(first_file[key], second_file[key])
            diff.append({
                'key': key,
                'status': 'inner node',
                'value': child
            })

        elif is_equal_items(first_file, second_file, key):
            diff.append({
                'key': key,
                'status': 'equal',
                'value': first_file[key]
            })

        elif is_not_equal_items(first_file, second_file, key):
            diff.append({
                'key': key,
                'operation': 'changed',
                'value': (first_file[key], second_file[key])
            })

        elif key in first_file:
            diff.append({
                'key': key,
                'status': 'deleted',
                'value': first_file[key]
            })

        elif key in second_file:
            diff.append({
                'key': key,
                'status': 'added',
                'value': second_file[key]
            })

    return diff

print(generate_diff())

    # with open('files/output.txt', 'w+') as output:
    #     output.write('{\n')
    #     for key in all_keys:
    #         if tools.is_equal_item(first_file, second_file, key):
    #             output.write(tools.get_string_line(first_file, key, 'Equal'))
    #         elif key in first_file and key in second_file:
    #             output.write(tools.get_string_line(first_file, key, 'Delete'))
    #             output.write(tools.get_string_line(second_file, key, 'Adding'))
    #         elif key in first_file:
    #             output.write(tools.get_string_line(first_file, key, 'Delete'))
    #         elif key in second_file:
    #             output.write(tools.get_string_line(second_file, key, 'Adding'))
    #     output.write('}')

    #     output.seek(0)
    #     diff = output.read()
    #     print(diff)

    # return diff
