'''
Problem
-------------------
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.\
int[] reset() Resets the array to its original configuration and returns it.\
int[] shuffle() Returns a random shuffling of the array.\

Constraints
-------------------
1 <= nums.length <= 200\
-10^6 <= nums[i] <= 10^6\
All the elements of nums are unique.\
At most 5 * 10^4 calls in total will be made to reset and shuffle.\

Thinking
-------------------
* There are 5 * 10^4 calls in total, so the time complexity for each should be at most O(nlogn), n is the length of the array. Since all
  all the call can be made either to reset and shuffle.

* And we need to ensure all permutations of the array should be equally likely  

* We could do this gradually
    * For index 0, we choose a random number from 0 to len(arr) - 1, we swap arr[random_number] with arr[0]
    * For index 1, we continue to do this: from 1 to len(arr) - 1, swap arr[random_number] with arr[1]
    * and so on...
    * Assume generating random number is O(1), we can do this in O(n), so the total complexity would be O(n * k), k is the number of calls, could work!

* From my intuition, this creates a equally likely shuffle. It's like choosing balls from a bag, the sequence is completely random. So each sequence should be equal likely
    * Also this can be proved by computing exact probablity
'''
from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        new_arr = self.arr[:]

        def swap(i, j):
            temp = new_arr[i]
            new_arr[i] = new_arr[j]
            new_arr[j] = temp
        for i in range(len(new_arr)):
            random_index = random.randint(i, len(new_arr) - 1)
            swap(i, random_index)
        return new_arr


if __name__ == "__main__":
    nums = [1, 2, 3]
    obj = Solution(nums)
    result_1 = obj.reset()
    result_2 = obj.shuffle()
    result_3 = obj.reset()
    result_4 = obj.shuffle()
    print(result_1, result_2, result_3, result_4)
