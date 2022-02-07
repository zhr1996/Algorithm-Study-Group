'''
Problem
-------------------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Constraints
-------------------
* 1 <= nums.length <= 100
* 0 <= nums[i] <= 400

Thinking
-------------------
* memorziation
    * rob(i) is the maximum money get after robbing i houses (not necessarily robbed all houses)
    * transition function rob(i):
        * money(i) + rob(i-2)
        * rob(i-1)
    * base,
        * rob(0) = money(0), the maximum money get from one house is always gained by robbing the course
        * rob(<0) = 0, no house to rob for
'''
from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    memory = [-1] * n

    def rob_helper(i):
        if i < 0:
            return 0
        if memory[i] != -1:
            return memory[i]
        max_money = max(rob_helper(i-1), rob_helper(i-2) + nums[i])
        memory[i] = max_money
        return max_money
    rob_helper(n-1)
    return memory[-1]


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))
