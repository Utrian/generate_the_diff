import os.path
from engine.tools import (
                            normalize_bool,
                            is_nested_structure
)


def get_message(ancestry, status, value):
    common_part = f'Propertry {ancestry} was'

    if status == 'updated':
        pre_value, new_value = value
        return f'{common_part} updated. From {pre_value} to {new_value}'

    if status == '+':
        return f'{common_part} added with value: {value}'
    
    if status == '-':
        return f'{common_part} removed'


def plain(diff: dict, path_output='files/output.txt'):
    output = open(path_output, 'w')

    pre_value = None
    pre_status = None

    def walk(diff, pre_ancestry):
        diff = iter(diff.items())
        for key, value in diff:
            new_key = key[4:]
            new_status = key[2]
            new_ancestry = os.path.join(pre_ancestry, new_key)

            if is_nested_structure(value): #должен быть в каждой итерации
                
                if new_status != ' ':
                    value = '[complex value]'
                    
                walk(value, new_ancestry)
                continue

            if pre_ancestry == new_ancestry:
                output.write(get_message(
                                        pre_ancestry,
                                        'updated',
                                        (pre_value, value)
                ))

                continue

            try: #блок для обычный итерации, где параметр был только удален или добавлен
                next(diff)

                output.write(get_message(
                                        pre_ancestry,
                                        pre_status,
                                        pre_value
                ))

            except (StopIteration, TypeError): #блок для самой последней итерации
                output.write(get_message(
                    new_ancestry,
                    new_status,
                    value
                ))


    walk(diff, '')
    output.close()

    with open(path_output, 'r') as f:
        return f.read()


print(plain({'    common': {'  + follow': False, '    setting1': 'Value 1', '  - setting2': 200, '  - setting3': True, '  + setting3': None, '  + setting4': 'blah blah', '  + setting5': {'    key5': 'value5'}, '    setting6': {'    doge': {'  - wow': '', '  + wow': 'so much'}, '    key': 'value', '  + ops': 'vops'}}, '    group1': {'  - baz': 'bas', '  + baz': 'bars', '    foo': 'bar', '  - nest': {'    key': 'value'}, '  + nest': 'str'}, '  - group2': {'    abc': 12345, '    deep': {'    id': 45}}, '  + group3': {'    deep': {'    id': {'    number': 45}}, '    fee': 100500}}))