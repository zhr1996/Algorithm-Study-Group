# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example 1:
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# This problem is using dedup, and I found drawing a state tree really helpful

# Don't forget to add in an empty set

# State: 1. current combination so far 2. start index of candidate 3. result array to store results
# return nothing
# Each backtraking is pushing an element into cur, and then later after got returned from all the stack above, pop the current element to try other
# candidate

from typing import List

# Base case, start_index = len(nums), means every combination is tried already


def helper(nums, start_index, cur, result):
    if start_index == len(nums):
        return

    for i in range(start_index, len(nums)):
        cur.append(nums[i])
        # Remeber the start index for next recursion is current iterating index
        helper(nums, i + 1, cur, result)
        # Add in current combination to result
        result.append(cur[:])
        cur.pop()
    return


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    result.append([])
    helper(nums, 0, [], result)
    return result


if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    result = subsets(nums)
    result.sort()
    for res in result:
        print(' '.join(str(num) for num in res))
