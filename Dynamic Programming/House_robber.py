from typing import List

# Each house has a certain amount of treasure stashed, the only constraint stopping you from robbing every one of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Think dp as multistage optimization
# For house at index i, we could take the treasure, but in that case we can't take the treasure of house at index i - 1
# nums[i] + dp[i-2]
# Another option, is we don't take the treasure, in this situation, we can take treasure of house at index i - 1
# dp[i-1]


def rob(nums: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    dp = [0 for x in range(len(nums))]
    dp[0] = nums[0]
    if len(nums) == 1:
        return dp[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    return dp[-1]


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    print(rob(numbers))
