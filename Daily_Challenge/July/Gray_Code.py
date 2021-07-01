'''
Problem
-------------------
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.

1 <= n <= 16

Thinking
-------------------
* One bit difference between each code. Would add one bit work? no 01 + 1 = 10, so add is definitely wrong

* So how to make one bit difference?

* Solving this needs to remember one observation: only when ith bit and i+1th bit of n differ will ith bit of gray code of n be 1, otherwise 
  it is 0. In other words, if ith bit and i+1th bit of n are euqal, then ith bit of gray code of n is 0

* Very interesting problem! The basic of gray code is easy, but to come up with an algorithm to generate them is actually hard, specifically 
  if I don't remember about any observations about gray code

'''
from typing import List


def grayCode(n: int) -> List[int]:
    def gray(num):
        return num ^ (num >> 1)

    gray_code = [-1 for x in range(2 ** n)]

    for i in range(2 ** n):
        gray_code[i] = gray(i)
    return gray_code


if __name__ == "__main__":
    print(grayCode(3))
