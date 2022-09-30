from gen_diff import generate_diff
from tools import get_string_line

DIFF = generate_diff()


def stylish():

    with open('files/output.txt', 'w') as output:
        output.write('{')

        for node in DIFF:
            if isinstance(node['value'], list):
                output.write(get_string_line(node))
        output.write('}')



def print_diff():
    for key in DIFF:
        print(key, '\n')

stylish()
print_diff()