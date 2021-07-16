'''
Problem
-------------------
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n\
a, b, c, and d are distinct.\
nums[a] + nums[b] + nums[c] + nums[d] == target\
You may return the answer in any order.\

Constraints
-------------------
1 <= nums.length <= 200\
-10^9 <= nums[i] <= 10^9\
-10^9 <= target <= 10^9\

Thinking
-------------------
* Brute Force: iterate through the array, find four numbers that sum up to target: O(n^4) TLE

* Convert it into two sum by summing up all possible distinct pairs?
    * Store them in a dictionary. Use sum as the key, and the pair tuple as value.
        * To avoid the situation that pair_sum = target // 2 (this will take the same pair twice as a potential answer), 
        keep a state variable to see whehter it is the first time that meets the target // 2.
        * Or store the index instead of the arr nums. Since in this way, index will always be distinct. If the tuple is the same, we can safely assume it's the same and skip
        * This is wrong, it doesn't preventing using the same number twice! We have to check if there are same index in the four indexes!
    * To avoid repeatness, store the result nums in ascending order and as a tuple in a set
    * Time complexity:
        * Convert to hashmap: O(n^2)
        * Find two sum O(n)
        * Overall: O(n^2)


'''
from typing import List
from collections import defaultdict


def fourSum(nums: List[int], target: int) -> List[List[int]]:

    all_pairs_sum = defaultdict(list)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            all_pairs_sum[nums[i] + nums[j]].append((i, j))

    all_possible_solution_set = set()
    for sum in all_pairs_sum:
        if target - sum in all_pairs_sum:
            for pair1 in all_pairs_sum[sum]:
                for pair2 in all_pairs_sum[target - sum]:
                    if pair1 == pair2:
                        continue
                    index1, index2 = pair1
                    index3, index4 = pair2
                    if index1 in set((index3, index4)) or index2 in set((index3, index4)):
                        continue

                    all_possible_solution_set.add(
                        tuple(sorted([nums[index1], nums[index2], nums[index3], nums[index4]])))

    all_solution_arr = []
    for solution in all_possible_solution_set:
        num1, num2, num3, num4 = solution
        all_solution_arr.append([num1, num2, num3, num4])
    return all_solution_arr


if __name__ == "__main__":
    print(fourSum([1, 0, -1, 0, -2, 2], 0))
