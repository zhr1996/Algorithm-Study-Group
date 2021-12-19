'''
Problem
-------------------
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Constraints
-------------------
* 1 <= arr.length <= 10^4
* 1 <= arr[i] <= 10^5

Thinking
-------------------
* start from the end, keep a state variable of the largest number to the right and replace current number with the largest number

'''
from typing import List


def replaceElements(arr: List[int]) -> List[int]:
    largest_num_seen = -1
    for i in range(len(arr)-1, -1, -1):
        temp = arr[i]
        arr[i] = largest_num_seen
        if temp > largest_num_seen:
            largest_num_seen = temp
    return arr


if __name__ == "__main__":
    input_list = [17, 18, 5, 4, 19, 1]
    print(replaceElements(input_list))
    print(input_list)
