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
    * For each element in array, we iterate through all possible length and compare it with dp[j-1], if it is greater than dp[j-1], then it can form a length of j increasing subsequence, so update dp[j] = a[i]
    * since we are always keep the smallest element of length j, we should also check to only update when a[i] < dp[j]
    *
'''
from typing import List
from bisect import bisect_left


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


# Time complexity: O(nlogn)
# First implement according to second way. And then improve with binary search
def lengthOfLIS_v2(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    dp = [float("inf") for x in range(len(nums) + 1)]
    dp[0] = -float("inf")
    for i in range(0, len(nums)):
        # Use binary search. Here we can find the first element strictly greater than arr[i]
        # This is strictly smaller than len(arr). It can't be greater, so we can safely update dp[j]
        j = bisect_left(dp, nums[i])
        dp[j] = nums[i]
        # for j in range(1, len(nums) + 1):
        #     if nums[i] > dp[j-1] and nums[i] < dp[j]:
        #         dp[j] = nums[i]
    length_of_LIS = 1
    for i in range(1, len(nums) + 1):
        if dp[i] < float("inf"):
            length_of_LIS = i
    return length_of_LIS


if __name__ == "__main__":
    print(lengthOfLIS_v2([10, 9, 2, 5, 3, 7, 101, 18]))
