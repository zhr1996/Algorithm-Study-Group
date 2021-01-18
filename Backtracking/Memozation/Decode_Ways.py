# We have a message to decode. Letters are encoded to digits by its position in the alphabet

# A -> 1
# B -> 2
# C -> 3
# ...
# Y -> 25
# Z -> 26
# Given a non-empty string of digits, how many ways are there to decode it?

# Input: "18"

# Output: 2

# Explanation: "18" can be decoded as "AH" or "R"

# Input: "123"

# Output: 3

# Combinational Search Problem, how many way there are to combine those digits?

# State: current digits processing
# return : number of ways to decode str[index:]

import time


def helper_without_memo(digits, index, list_letter):
    if index == len(digits):
        return 1

    ways = 0
    remaining = digits[index:]
    for letter in list_letter:
        if remaining.startswith(letter):

            ways += helper_without_memo(digits,
                                        index + len(letter), list_letter)

    return ways

# Some overlapping problems that are solved during first recursion
# memoziation


def helper(digits, index, list_letter, memo):
    if index == len(digits):
        return 1
    if index in memo:
        return memo[index]
    ways = 0
    remaining = digits[index:]
    for letter in list_letter:
        if remaining.startswith(letter):

            ways += helper(digits, index + len(letter), list_letter, memo)
    memo[index] = ways
    return ways


def decode_ways(digits):
    list_letter = [str(x) for x in range(1, 27)]
    memo = {}
    return helper_without_memo(digits, 0, list_letter)
    # return helper(digits, 0, list_letter, memo)


if __name__ == "__main__":
    digits = input()
    start_time = time.time()
    print(decode_ways(digits))
    print("--- %s seconds ---" % (time.time() - start_time))
