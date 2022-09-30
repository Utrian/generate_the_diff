from gendiff.tools import (
    get_files, is_equal_items,
    is_inner_node, is_inner_nodes,
    is_not_equal_items, get_inner_data
)


def generate_diff(file_1=None, file_2=None):
    if file_1 is None and file_2 is None:
        file_1, file_2 = get_files()

    def walk(file_1, file_2, current_lvl):
        diff = list()
        all_keys = sorted(list(
            set(file_1.keys()) | set(file_2.keys())
        ))

        for key in all_keys:
            if key in file_1 and key in file_2:

                if is_equal_items(file_1, file_2, key):
                    if is_inner_nodes(file_1, file_2, key):
                        child = walk(file_1[key], file_2[key], current_lvl + 1)
                        diff.append(
                            get_inner_data(key, 'inner', 'equal', current_lvl, child)
                        )
                        continue

                    diff.append(
                        get_inner_data(key, 'leaf', 'equal', current_lvl, file_1[key])
                    )

                elif is_not_equal_items(file_1, file_2, key):
                    if is_inner_nodes(file_1, file_2, key):
                        child = walk(file_1[key], file_2[key], current_lvl + 1)
                        diff.append(
                            get_inner_data(key, 'inner', 'equal', current_lvl, child)
                        )
                        continue

                    diff.append(
                        get_inner_data(
                            key, 'leaf', 'changed', current_lvl,
                            (file_1[key], file_2[key])
                        )
                    )

            elif key in file_1:
                diff.append(
                    get_inner_data(key, 'leaf', 'deleted', current_lvl, file_1[key])
                )

            elif key in file_2:
                diff.append(
                    get_inner_data(key, 'leaf', 'added', current_lvl, file_2[key])
                )

        return diff
    return walk(file_1, file_2, 1)


print(generate_diff())