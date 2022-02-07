'''
Problem
-------------------
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

Constraints
-------------------
* 1 <= n, k <= 30
* 1 <= target <= 1000

Thinking
-------------------
* top down
    * use i dices to roll sum to target 
    * ways_to_roll(i, j) returns ways to roll i dices to sum j

* base case
    * i == len(dice)
        * if j == 0, return 1
        * if j != 0 , return 0 (not a successful way)

* transition
    * ways_to_roll(i,j) = 
        * sum of ways_to_roll(i+1, j - z), for z in range(1, k)
'''
from typing import List


def numRollsToTarget(n: int, k: int, target: int) -> int:
    dp = {}
    mod = 1000000000 + 7

    def ways_to_roll(i, j):
        # base case
        if i == n:
            if j == 0:
                return 1
            return 0

        # prune the branch
        if j <= 0:
            return 0

        # if in memory
        if (i, j) in dp:
            return dp[(i, j)]

        # transition
        sum_of_way = 0
        for z in range(1, k+1):
            # current dice result is z
            sum_of_way += ways_to_roll(i+1, j-z)

        dp[(i, j)] = sum_of_way
        sum_of_way %= mod
        return sum_of_way
    ret = ways_to_roll(0, target)
    return ret


if __name__ == "__main__":
    print(numRollsToTarget(2, 6, 7))
