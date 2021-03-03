class Solution:
    # Think of building a chain, keep a state variable to remember the global optimum, and think what would disrupt the chain
    def maxSubArray(self, nums: List[int]) -> int:
        prev_sum = nums[0]
        max_result = nums[0]
        for i in range(1, len(nums)):
            if prev_sum >= 0:
                prev_sum += nums[i]

            else:
                prev_sum = nums[i]

            max_result = max(prev_sum, max_result)
        return max_result
