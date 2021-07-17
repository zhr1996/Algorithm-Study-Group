'''
Problem
-------------------
You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

arr[0], arr[1], ..., arr[i] is the first part,\
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and\
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.\
All three parts have equal binary values.\
If it is not possible, return [-1, -1].\

Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

Constraints
-------------------
3 <= arr.length <= 3 * 10^4\
arr[i] is 0 or 1\

Thinking
-------------------
* Brute Force: start i from the first possible interval, start j from the second interval, try every possible pairs:
    * Time Complexity: O(n^2) TLE

* Observation: 
    * If there is a possible partition, then 1 will always be distributed evenly between the groups.

    * Since binary expression is unique for each number, then if the binary numbers are the same, the only difference between each group is the leading zero

    * The binary number is the same as the last parition of numbers

    * How to tell if they have the same patterns?
        * Regular expression
        * First find how many 1s are there in the string. If it can't be divided by 3 then return [-1,-1]
            * If can be divided by three, then find the start of last group of 1s, suppose index is k, use arr[k:] as the pattern
        * But regular expression can only tell whether the arr can be partitioned into 3 parts, it can't find the index of partition

    * Find the three parts of 1 first and then first compare the pattern.
        * If the patterns are the same, then count how many zeros there are after the third part. If there are enough zeros after the first part and second part. Then the parition is possible.

* Note:
    * Don't get impatient when doing this kind of questions. Just calm down and think about the problem.
    * The key here is don't think about the preceding zeros. Just think about how many zeros there are after the third pard. This is IMPORTANT!
'''
from typing import List


def threeEqualParts(arr: List[int]) -> List[int]:
    num_of_ones = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            num_of_ones += 1

    if num_of_ones % 3 != 0:
        return [-1, -1]

    if num_of_ones == 0:
        return [0, 2]
    ones_in_each_part = num_of_ones // 3

    i_1 = j_1 = i_2 = j_2 = i_3 = j_3 = 0

    count = 0

    # print(ones_in_each_part)
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            if count == 1:
                i_1 = i
            if count == ones_in_each_part:
                j_1 = i
            if count == ones_in_each_part + 1:
                i_2 = i
            if count == 2 * ones_in_each_part:
                j_2 = i
            if count == 2 * ones_in_each_part + 1:
                i_3 = i
            if count == 3 * ones_in_each_part:
                j_3 = i
    # print(i_1, j_1, i_2, j_2, i_3, j_3)
    if not(arr[i_1:j_1 + 1] == arr[i_2:j_2 + 1] == arr[i_3:j_3+1]):
        # print("here")
        return [-1, -1]

    trailing_zeros_in_third_part = len(arr) - j_3 - 1

    if i_2 - j_1 - 1 < trailing_zeros_in_third_part or i_3 - j_2 - 1 < trailing_zeros_in_third_part:
        return [-1, -1]

    return [j_1 + trailing_zeros_in_third_part, j_2 + trailing_zeros_in_third_part + 1]


if __name__ == "__main__":
    print(threeEqualParts([0, 0, 0]))
