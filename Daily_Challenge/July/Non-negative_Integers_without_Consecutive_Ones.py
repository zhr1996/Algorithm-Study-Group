'''
Problem
-------------------
Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

Constraints
-------------------
1 <= n <= 109

Thinking
-------------------
* Simple expression and few contraints always lead to hard problems

* Didn't have a clue after trying to think about 15 minutes. Tried a few observations, but doesn't work.

* Solution: https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/solution/

* 
'''
from typing import List


def findIntegers(n: int) -> int:
    f = [0 for i in range(32)]
    f[0] = 1
    f[1] = 2
    for i in range(2, len(f)):
        f[i] = f[i-1] + f[i-2]
    i = 30
    sum = 0
    prev_bit = 0
    while i >= 0:
        if n & (1 << i) != 0:
            sum += f[i]
            if prev_bit == 1:
                sum -= 1
                break
            prev_bit = 1
        else:
            prev_bit = 0
        i -= 1
    return sum + 1


if __name__ == "__main__":
    print(findIntegers(5))
