'''
Problem
-------------------
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

* arr.length >= 3
* There exists some i with 0 < i < arr.length - 1 such that:
    * arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Constraints
-------------------
* 1 <= arr.length <= 10^4
* 0 <= arr[i] <= 10^4

Thinking
-------------------
* keep two state variables: seen_increase and seen_decrease
    * if next num is larger then current number, 
        * if already seen decrease, then return False
        * set seen_increase to True
    * if next num is smaller,
        * if not seen increase, return False
        * set seen_decrease to True
    * if any time seen two nums are equal, return False
        * since all relation is either strict smaller or strict larger
* return True in the end if both seen_increase and seen_decrease

* another way: walk up then walk down
'''
from typing import List


def validMountainArray(arr: List[int]) -> bool:
    n = len(arr)
    i = 0

    while i + 1 < len(arr) and arr[i] < arr[i+1]:
        i = i + 1

    # if i is begining or ending
    if i == 0 or i == len(arr) - 1:
        return False

    # walk down
    while i + 1 < len(arr) and arr[i] > arr[i+1]:
        i = i + 1

    return i == len(arr) - 1


if __name__ == "__main__":
    print(validMountainArray([0]))
