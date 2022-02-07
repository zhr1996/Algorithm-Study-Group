'''
Problem
-------------------
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Constraints
-------------------
* 1 <= heights.length <= 100
* 1 <= heights[i] <= 100

Thinking
-------------------
* sort the array, compare the numbers at the same index for the two arrays .

* if they are different, add one to the final answer

* Time complexity: O(nlogn)

* bucket sort
    * create an array of length 100 (the range of heights are [0,100])
    * add 1 to the bucket if there is a number in the array is equal to the index of bucket
    * from 1 to 100, 


'''
from typing import List


def heightChecker(heights: List[int]) -> int:
    sorted_height = sorted(heights)
    num_of_index_diff = 0
    for i in range(len(heights)):
        if heights[i] != sorted_height[i]:
            num_of_index_diff += 1
    return num_of_index_diff


def heightChecker_2(heights: List[int]) -> int:
    bucket_array = [0 for i in range(101)]
    for num in heights:
        bucket_array[num] += 1

    index = 0

    bucket_index = 1

    num_of_index_diff = 0

    while bucket_index <= 100:
        if bucket_array[bucket_index] != 0:
            if heights[index] != bucket_index:
                num_of_index_diff += 1

            # move one step to the right in both arrays
            bucket_array[bucket_index] -= 1
            index += 1
        else:
            bucket_index += 1
    return num_of_index_diff


if __name__ == "__main__":
    print(heightChecker_2([1, 3, 1, 1]))
