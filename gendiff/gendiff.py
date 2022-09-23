from gendiff.tools import tools


def generate_diff():
    first_file, second_file = tools.get_files()
    all_keys = sorted(
        [key for key in first_file] +
        [key for key in second_file if key not in first_file]
    )

    with open('files/output.txt', 'w+') as output:
        output.write('{\n')
        for key in all_keys:
            if tools.is_equal_item(first_file, second_file, key):
                output.write(tools.get_string_line(first_file, key, 'Equal'))
            elif key in first_file and key in second_file:
                output.write(tools.get_string_line(first_file, key, 'Delete'))
                output.write(tools.get_string_line(second_file, key, 'Adding'))
            elif key in first_file:
                output.write(tools.get_string_line(first_file, key, 'Delete'))
            elif key in second_file:
                output.write(tools.get_string_line(second_file, key, 'Adding'))
        output.write('}')

        output.seek(0)
        diff = output.read()
        print(diff)

    return diff
