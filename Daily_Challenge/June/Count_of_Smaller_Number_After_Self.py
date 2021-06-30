'''
Problem
-------------------
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

1 <= nums.length <= 105
-104 <= nums[i] <= 104

Thinking
-------------------
* The maximum length is 10^5, so a O(N^2) solution is not suitable (compare each number to the list after it)

* The one is hard

* Solution
    * Segment Tree
    * Binary Index Tree
    * Merge Sort

'''
from typing import List


def countSmaller(nums: List[int]) -> List[int]:
    # implement Binary Index Tree
    def update(index, value, tree, size):
        index += 1  # index in BIT is 1 more than the original index
        while index < size:
            tree[index] += value
            index += index & -index

    def query(index, tree):
        # return sum of [0, index)
        result = 0
        while index >= 1:
            result += tree[index]
            index -= index & -index
        return result

    offset = 10**4  # offset negative to non-negative
    size = 2 * 10**4 + 2  # total possible values in nums plus one dummy
    tree = [0] * size
    result = []
    for num in reversed(nums):
        smaller_count = query(num + offset, tree)
        result.append(smaller_count)
        update(num + offset, 1, tree, size)
    return result[::-1]


if __name__ == "__main__":
    print(countSmaller([5, 2, 6, 1]))
