import gendiff.formatters.stylish as ft_stylish
import gendiff.formatters.plain as ft_plain
import gendiff.formatters.json as ft_json


def formatting(unformatted_diff: list, ft_name: str):
    formatters = {
        'stylish': ft_stylish.stylish,
        'plain': ft_plain.plain,
        'json': ft_json.diff_to_json
    }

    if ft_name in formatters:
        formatter = formatters[ft_name]
        return formatter(unformatted_diff)

    raise NameError('Incorrect formatter name ({ft_name}).')
