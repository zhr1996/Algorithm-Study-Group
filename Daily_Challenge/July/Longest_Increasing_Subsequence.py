'''
Problem
-------------------
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Constraints
-------------------
1 <= nums.length <= 2500   
-104 <= nums[i] <= 104

Thinking
-------------------
* Dynamic Programming. But what should be stored in the dp array?

* Brute force, start from each num, and to see what's the logenst increasing subsequence
    * But how to determine which choice is the longest increasing subsequence? Backtracking
    * Since each one greater than current is a choice, then time complexity is nearly O(n * 2^n)

* But if I know the subresult, which is the lognest increasing before, I can easily find current longest subsequence by: max(dp[k_1], dp[k_2],... dp[k_n]) + 1 (k_i is smaller than current number: arr[i])
    * So we could gradually build up the optimal result. Keep a state variable storing the longest sequence along traverse.
    * Time Complexity: O(n^2)
    * Space Complexity: O(n)

* Optimization:
    * We could store a sorted dictionary, and find the first larger one in O(logn) (left all smaller than current)
        * But still need to compare all these LTS
    * To achieve O(nlogn), we need to change the information stored in dp array. Instead of storing the longest length, we store the smallest elements which ends a length i subsequence.
'''
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    dp = [0 for x in range(len(nums))]
    longest_LTS_length = 1
    dp[0] = 1
    for i in range(1, len(nums)):
        cur_max = 1
        for j in range(0, i):
            if nums[j] < nums[i]:
                cur_max = max(cur_max, dp[j] + 1)
        dp[i] = cur_max
        longest_LTS_length = max(longest_LTS_length, cur_max)
    return longest_LTS_length


if __name__ == "__main__":
    print(lengthOfLIS([-2]))
