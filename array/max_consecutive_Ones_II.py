'''
Problem
-------------------
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Constraints
-------------------
* 1 <= nums.length <= 105
* nums[i] is either 0 or 1.

Thinking
-------------------
* Dynamic Programming, (seems not the right approach)
    * two states, index of the array and whether already flipped a zero

* max_consecutive_one(index, has_flipped) =
    * if nums[index] = 1,
        * 1 + max_consecutive_one(index-1, has_flipped)

* Brute Force
    * Iterate array from start to end, choose each index as the start of thea rray
    * Use a second pointer to loop (first_pointer, end), count how many 0s in (first_pointer, second_pointer)
    * Update max_consecutive_one if the number of zeros are smaller or equal to 1
    * if num_of_zero larger than 1, break

* sliding window
    * expand the window and do the flip until reaches a invalid state
    * shrink the window so the window is valid again

* sliding window is used when asked to find an optimal sub-structure
'''
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_consecutive_one = 0
    for left in range(0, len(nums)):
        num_of_zero = 0
        consecutive_one = 1
        for right in range(left, len(nums)):
            if nums[right] == 0:
                num_of_zero += 1
            else:
                consecutive_one += 1
            if num_of_zero > 1:
                break

            max_consecutive_one = max(max_consecutive_one, consecutive_one)
    return max_consecutive_one


def findMaxConsecutiveOnes_slide_window(nums: List[int]) -> int:
    max_consecutive_one = 0
    window_start = 0
    window_end = 0

    num_of_zero_filpped = 0

    for window_end in range(len(nums)):
        if nums[window_end] == 0:
            num_of_zero_filpped += 1
            while num_of_zero_filpped > 1:
                # while the window is still in invalid state, shrink the window to make the window valid
                if nums[window_start] == 0:
                    num_of_zero_filpped -= 1
                window_start += 1
        # compare the valid state window lenght with the max consecutive window we get so far
        max_consecutive_one = max(
            max_consecutive_one, window_end - window_start + 1)

    return max_consecutive_one


if __name__ == "__main__":
    print(findMaxConsecutiveOnes_slide_window(
        [0, 0, 1]))
