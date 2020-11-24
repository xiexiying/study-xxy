"""
罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。
"""


def roman_to_arab(str_target):
    res = 0
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(str_target) - 1):
        if roman_dict[str_target[i]] < roman_dict[str_target[i + 1]]:
            res -= roman_dict[str_target[i]]
        else:
            res += roman_dict[str_target[i]]
    res += roman_dict[str_target[-1]]
    return res

print(roman_to_arab("X"))
