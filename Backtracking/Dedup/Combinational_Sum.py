# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Examples
# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.

# 7 is a candidate, and 7 = 7.

# These are the only two combinations.

# The most interesting in this problem is there shouln't be duplicate combinations, and this can be done by only considering possible candidates after the current one
# For example, in example 1, one possible duplication is [2,2,3] and [3,2,2]. In this case, we shouldn't consider substracting 2 because all cases involving substracting 2 has
# already been explored in the first state tree traverse

# State: 1. start index of candidates 2. remaining of target 3. the result array
# Return: Nothing

from typing import List


# base case, remaining = 0 or < 0
def helper(candidates, start_index, remaining, cur, result):
    if remaining == 0:
        result.append(cur[:])
        return
    n = len(candidates)
    for i in range(start_index, n):
        num = candidates[i]
        if remaining - num >= 0:
            cur.append(num)
            # start index changed to i, because the next number could be the same number
            helper(candidates, i, remaining - num, cur, result)
            # backtracking, trying out next candidate
            cur.pop()
    return


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    helper(candidates, 0, target, [], result)
    return result


if __name__ == "__main__":
    candidates = [int(x) for x in input().split()]
    target = int(input())
    result = combinationSum(candidates, target)
    for res in result:
        print(' '.join(str(num) for num in res))
