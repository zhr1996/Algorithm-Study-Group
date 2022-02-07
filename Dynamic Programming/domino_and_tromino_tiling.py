'''
Problem
-------------------
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

Constraints
-------------------
* 1 <= n <= 1000

Thinking
-------------------
* top down

* num_of_way(i)
    * number of ways to fill 2 * i board

* base case
    * i == 0, return 1
    * i < 0, return 0

* transition    
    * there are three basic ways of filling
        * two horizontal tile to fill 2 * 2 board
        * 1 verticle tile to fill 2 * 1 board
        * two tromino tile to fill 2 * 3 board
    * so at each stage, we have three possibilities to fill
        * sum_of_way(i) = sum(sum_of_way(i-1) * 1, ...(i-2) * 1, ...(i-3) * 2)

* improvement
    * have two functions, f(x) is to fill exactly 1 * x boards
    * p(x) is fill 1 * x boards, but one cell is empty (could be the top or the borrom rightmost cell)
    * transition
        * like analysisd above, f(x) = f(x-1) + f(x-2)
        * p(x) = f(x-2) + p(x-1)
            * either put a trimo to a exactly filled board
            * or put a dimo to a partially filled board
    * 
'''
from typing import List
from functools import lru_cache


def numTilings(n: int) -> int:

    @lru_cache(None)
    def f(x):
        # base case
        if x <= 2:
            return x

        # trim the branch
        if x < 0:
            return 0

        return f(x-1) + f(x-2) + 2 * p(x-1)

    @lru_cache(None)
    def p(x):
        # base case
        if x == 2:
            return 1

        # trim branch
        if x < 2:
            return 0

        return f(x-2) + p(x-1)
    return f(2)


if __name__ == "__main__":
    print(numTilings(4))
