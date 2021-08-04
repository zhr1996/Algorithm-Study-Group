'''
Problem
-------------------
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints
-------------------
1 <= nums.length <= 10
-10 <= nums[i] <= 10

Thinking
-------------------
* Simple description always leads to hard questions

* Backtracking, first sort the array, then add in a set to avoid duplicate

* Sorting is to prevent [1,2] and [2,1] exists at same time
'''
from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    result_set = set()

    nums.sort()

    def helper(index, cur):
        if index >= len(nums):
            return

        cur_num = nums[index]

        # Two choice, add in the number or don't add in this number

        # First add in this number
        temp_cur = cur[:]
        temp_cur.append(cur_num)
        result_set.add(tuple(temp_cur))
        helper(index + 1, temp_cur)

        # Second don't add in this number
        result_set.add(tuple(cur))
        helper(index + 1, cur)

    helper(0, [])
    # print(result_set)
    return [list(tuple_ele) for tuple_ele in list(result_set)]


if __name__ == "__main__":
    print(subsetsWithDup([1, 2, 2]))
