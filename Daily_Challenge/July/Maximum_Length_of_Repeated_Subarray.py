'''
Problem
-------------------
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Constraints
-------------------
1 <= nums1.length, nums2.length <= 1000

0 <= nums1[i], nums2[i] <= 100

Thinking
-------------------
* Reminds me of dynamic programming, maximum continue string? 

* Hints: Use dynamic programming. dp[i][j] will be the answer for inputs A[i:], B[j:].

* Use a dp array to store the sub results,
    * dp[i][j] stores the maximum subarray appears both in A[i:] and B[j:]
    * So the final return value is dp[0][0]
    * We can start from the end of the array:
        * dp[len(A) - 1][len(B) - 1] = bool(A[-1] == B[-1])
        * I think there is something not clear about the hints. dp[i][j] should represent the answer that start exactly form i and j
          If not, there is no clear state transferring equations
        * dp[i][j] = 
            * if A[i] == B[j], dp[i][j] = dp[i+1][j+1] + 1
            * else, dp[i][j] = 0
            * In each iteration, compare to see if dp[i][j] is larger than current maximum
        * return maximum dp[i][j]

Optimization
-------------------
* Instead using 2-d array, we can switch to 1-d array

'''
from typing import List


def findLength(nums1: List[int], nums2: List[int]) -> int:
    # dp = [[0 for j in range(len(nums2) + 1)] for i in range(len(nums1) + 1)]
    prev_dp = [0 for j in range(len(nums2) + 1)]
    maximum_subarray_length = 0
    for i in range(len(nums1) - 1, -1, -1):
        cur_dp = [0 for j in range(len(nums2) + 1)]
        for j in range(len(nums2) - 1, -1, -1):
            if nums1[i] == nums2[j]:
                cur_dp[j] = prev_dp[j+1] + 1
                maximum_subarray_length = max(
                    maximum_subarray_length, cur_dp[j])
        prev_dp = cur_dp
    return maximum_subarray_length


if __name__ == "__main__":
    print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
