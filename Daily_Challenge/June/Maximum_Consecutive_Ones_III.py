'''
Problem
-------------------
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


Thinking
-------------------
* backtracking all possible ways and count each possible way consecutive 1s

* sliding window: we are only flipping a 0 because it can extend 1s, for example, we won't flip the middle 0 in "000"

* Wacth for word consecutive in question

* At start of each loop, right pointer is tentative
'''
from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    left = 0
    right = 0

    num_of_zero = 0
    maximum_length = 0

    cur_window_size = 0
    while right < len(nums):
        if nums[right] == 0 and num_of_zero < k:
            num_of_zero += 1
        elif nums[right] == 0 and num_of_zero >= k:
            maximum_length = max(maximum_length, cur_window_size)
            while num_of_zero >= k:
                if nums[left] == 0:
                    num_of_zero -= 1
                left += 1
                cur_window_size -= 1
            # Add current 0
            num_of_zero += 1

        cur_window_size += 1
        right += 1
    maximum_length = max(maximum_length, cur_window_size)
    return maximum_length


if __name__ == "__main__":
    print(longestOnes([1, 1, 1, 0, 1, 1, 0, 1, 1], 1))
