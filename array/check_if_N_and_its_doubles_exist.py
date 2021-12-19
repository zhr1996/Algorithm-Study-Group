'''
Problem
-------------------
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Constraints
-------------------
* 2 <= arr.length <= 500
* -10^3 <= arr[i] <= 10^3

Thinking
-------------------
* use a set to take down every number we met, and check if there is double or half in the dictionary

* check both half and double, since we won't know which number is put into dictionary first
'''
from typing import List


def checkIfExist(arr: List[int]) -> bool:
    seen = set()
    for num in arr:
        if num * 2 in seen:
            return True
        if num % 2 == 0 and num // 2 in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    print(checkIfExist([10, 6, 7, 11, 2]))
