'''
Problem
-------------------
You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

* Choose one integer x from either the start or the end of the array nums.
* Add multipliers[i] * x to your score.
* Remove x from the array nums.
Return the maximum score after performing m operations.

Constraints
-------------------

* n == nums.length
* m == multipliers.length
* 1 <= m <= 10^3
* m <= n <= 10^5
* -1000 <= nums[i], multipliers[i] <= 1000

Thinking
-------------------
* optimal strategy, the previous actions affects the action later

* three state variables,
    * left index of number
    * right index of number
    * index of mutipler (how many operations we've done so far)

* can be compressed in to two state variables
    * left index , index of multiplier, since right index can be deduced from them
    * index of muliplier - i, indicates how many operations we have done
        * so i >= left, and numbers taken from right = i - left, right = n - 1 - (i - left)
    
* score_helper(i, left) = the highest score get from multiplier[i, :] and nums index at left
    * eventually we want to know score_helper(0,0)
    * transition function
        * score_helper(i,left) = max(
            * score_helper(i+1,left+1) + nums[left] * multiplier[i]
            * score_helper(i+1,left) + nums[right] * multiplier[i]
    * base case
        * if i >= m, return 0


'''
from typing import List
from functools import lru_cache


def maximumScore(nums: List[int], multipliers: List[int]) -> int:
    n = len(nums)
    m = len(multipliers)

    dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)]

    # initialize boundary
    # for j in range(m + 1):
    #     dp[m][j] = 0

    for i in range(m - 1, -1, -1):
        for left in range(i, -1, -1):
            right = n - 1 - (i - left)
            dp[i][left] = max(dp[i+1][left+1] + nums[left] *
                              multipliers[i], dp[i+1][left] + nums[right] * multipliers[i])
    return dp[0][0]


if __name__ == "__main__":
    print(maximumScore([1, 2, 3],
                       [3, 2, 1]))
