import stylish
from tools import (
    get_files, is_equal_items,
    is_inner_node, is_not_equal_items, get_inner_data
)


def external_walk(file, depth):
    diff = list()
    all_keys = sorted(list([key for key in file]))

    for key in all_keys:
        if is_inner_node(key, file):
            child = external_walk(file[key], depth + 1)
            diff.append(get_inner_data(key, 'equal', depth, child))
            continue

        diff.append(get_inner_data(key, 'equal', depth, file[key]))

    return diff


def generate_diff(file_1=None, file_2=None, formater=stylish.formater):
    if file_1 is None and file_2 is None:
        file_1, file_2 = get_files()

    def walk(file_1, file_2, depth):
        diff = list()
        all_keys = sorted(list(
            [key for key in file_1] +
            [key for key in file_2 if key not in file_1]
        ))

        for key in all_keys:
            if is_inner_node(key, file_1, file_2): #проверка на то что это не листовой узел для того чтобы идти дальше и каждому элементу дать его глубину, что поможет при форматировании
                child = walk(file_1[key], file_2[key], depth + 1)
                diff.append(
                    get_inner_data(key, 'equal', depth, child)
                )

            elif is_equal_items(file_1, file_2, key):
                diff.append(
                    get_inner_data(key, 'equal', depth, file_1[key])
                )

            elif is_not_equal_items(file_1, file_2, key):
                diff.append(
                    get_inner_data(
                        key, 'changed', depth,
                        (file_1[key], file_2[key])
                    )
                )

            elif key in file_1:
                if is_inner_node(key, file_1):
                    child = external_walk(file_1[key], depth + 1)
                    diff.append(
                        get_inner_data(key, 'deleted', depth, child)
                    )
                    continue

                diff.append(
                    get_inner_data(key, 'deleted', depth, file_1[key])
                )

            elif key in file_2:
                if is_inner_node(key, file_2):
                    child = external_walk(file_2[key], depth + 1)
                    diff.append(
                        get_inner_data(key, 'added', depth, child)
                    )
                    continue

                diff.append(
                    get_inner_data(key, 'added', depth, file_2[key])
                )

        return diff
    return walk(file_1, file_2, 1)
