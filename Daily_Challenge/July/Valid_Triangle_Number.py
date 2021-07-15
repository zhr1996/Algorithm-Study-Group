'''
Problem
-------------------
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Constraints
-------------------
1 <= nums.length <= 1000\
0 <= nums[i] <= 1000\

Thinking
-------------------
* Triangle: a + b > c 

* Idea 1:
    * First sort the array: O(nlogn)
    * Start from first element, take each element after it as a pair, use binary search to find the first element that is great or equal to (a + b)
        * Suppose now the second element in pair has index i, the first great element has index j, then the number of valid pair is (j - i - 1)
          Combination in between are all valid
        * Time complexity: O(n^2*logn)
        * A small optimization: Use an array to cache the search result. So Time could be reduced to O(n^2), but space is increased to O(n)
* Note the corner case of side length equal to zero
'''
from typing import List
import bisect


def triangleNumber(nums: List[int]) -> int:
    nums.sort()
    valid_pairs = 0

    for i in range(len(nums) - 2):
        if nums[i] == 0:
            continue
        for j in range(i + 1, len(nums) - 1):
            first_greater_or_equal_index = bisect.bisect_left(
                nums, nums[i] + nums[j])

            valid_pairs += first_greater_or_equal_index - j - 1
    return valid_pairs


if __name__ == "__main__":
    print(triangleNumber([0, 0, 1]))
