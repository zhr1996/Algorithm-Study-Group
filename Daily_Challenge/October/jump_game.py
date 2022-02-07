'''
Problem
-------------------
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Constraints
-------------------
* 1 <= nums.length <= 104

* 0 <= nums[i] <= 105

Thinking
-------------------
* The only way to stop a jumper from reaching the end is a zero in the road

* Jumpy as far as we can? but we miss on steps that can jump even further

* starting from first index, search in the jump range for the furthest jump
    * if find a further jump, update the furthest jump
        * if jump is longer than the length of array, return True
        * if all step is searched, but can't make further, return False since it can't jump further

* Time complexity: O(N), will it work?
'''
from typing import List


def canJump(nums: List[int]) -> bool:
    # length of array
    n = len(nums)

    # start to try jumping
    furtherest_jump = nums[0]
    index = 0

    # loop through all possible jumps
    while index <= furtherest_jump:
        if furtherest_jump >= n - 1:
            return True

        if index + nums[index] > furtherest_jump:
            furtherest_jump = index + nums[index]

        index += 1
    return False


if __name__ == "__main__":
    print(canJump([1, 2, 1, 0, 1]))
