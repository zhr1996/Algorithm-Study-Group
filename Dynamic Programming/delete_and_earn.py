'''
Problem
-------------------
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Constraints
-------------------
* 1 <= nums.length <= 2 * 10^4
* 1 <= nums[i] <= 10^4

Thinking
-------------------
* use a dictionary to store numbers and their occurrence

* oh my, I just realized this is exactly same problem with house robber
    * if I take this number, i can't take the numbers which is neighbor of it
    * ...

* earn_helper(i) - is max point we can get deleting i numbers (not necessary deleting all)
    * = max(earn_helper(i-1), earn_helper(i-2) + count * i)
    * i starts from 10,000

* base 
    * earn_helper( <= 0) = 0

* I think the hard part is to realize actually we need to iterate through from the largest number to the smallest numebr
'''
from typing import List
from collections import Counter


def deleteAndEarn(nums: List[int]) -> int:
    max_num = max(nums)
    count = [0] * (max_num + 1)
    for num in nums:
        count[num] += 1

    memory = [-1] * (max_num + 1)

    def earn_helper(i):
        if i <= 0:
            return 0
        if memory[i] != -1:
            return memory[i]
        max_earn = max(earn_helper(i-1), earn_helper(i-2) + i * count[i])
        memory[i] = max_earn
        return max_earn
    return earn_helper(max_num)


if __name__ == "__main__":
    print(deleteAndEarn([3, 3, 3, 4, 2]))
