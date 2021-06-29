'''
Problem
-------------------
Given an integer n, return true if and only if it is an Armstrong number.

The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.


1 <= n <= 10^8

Thinking
-------------------
* Brute force: adding up kth power of each digit and check if it equals the original number

'''
from typing import List


def isArmstrong(n: int) -> bool:
    str_num = str(n)

    k = len(str_num)

    power_sum = 0
    for i in range(len(str_num)):
        power_sum += int(str_num[i])**k

    return power_sum == n


if __name__ == "__main__":
    print(isArmstrong(123))
