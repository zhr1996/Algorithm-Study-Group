# Given a phone number contains 2-9, find all possible letter combinations the letter con translate into

# State:
# 1. current translation
# 2. current translating index of number

# return: nothing
# The result is stored in result parameter

from typing import List


def helper(digits, index, cur, result, mapping):
    if index == len(digits):
        # current is a possible answer
        result.append("".join(cur))
        return

    cur_digit = digits[index]
    if cur_digit not in mapping:
        return
    cur_list = mapping[cur_digit]
    for letter in cur_list:
        cur.append(letter)
        helper(digits, index + 1, cur, result, mapping)
        cur.pop()
    return result


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    result = []
    helper(digits, 0, [], result, mapping)
    return result


if __name__ == '__main__':
    combinations = letter_combinations_of_phone_number(input())
    print(' '.join(sorted(combinations)))
