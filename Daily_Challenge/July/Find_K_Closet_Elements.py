'''
Problem
-------------------
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

Thinking
-------------------
* Idea 1:Array is sorted in ascending order, this looks like a binary search problem

    * What if we first find the first smaller element than k and do a tentative look on both this and right number.
    * Then continuously append to result list till there are enough elements in the list
    * Time complexity: O(logN + N)
    * Space complexity: O(k)

* Idea 2:Or make use of priority queue. We push all the elements in it and the pop out the first k elements. The key is abs(num - k)
    * Time complexity: O(N*logN + k * logN)
    * Space complexity: O(N)

* Seems idea 1 has better time and space complexity. It makes sense since we are more clear on the target right then involve all the arrays

* Note bisect_left actually finds the first larger element in array. It's where the element should be inserted.
'''

from typing import List
from bisect import bisect_left


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    index_in_array = bisect_left(arr, x)
    count = 0
    left = index_in_array - 1
    right = index_in_array

    closest_k_elements = []
    while count < k:
        if left < 0:
            closest_k_elements.append(arr[right])
            right += 1
        elif right >= len(arr):
            closest_k_elements.append(arr[left])
            left -= 1
        else:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                closest_k_elements.append(arr[left])
                left -= 1
            else:
                closest_k_elements.append(arr[right])
                right += 1
        count += 1

    return sorted(closest_k_elements)


if __name__ == "__main__":
    print(findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5))
