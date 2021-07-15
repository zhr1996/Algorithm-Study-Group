'''
Problem
-------------------
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.

Constraints
-------------------
1 <= length <= 105\
0 <= updates.length <= 104\
0 <= startIdxi <= endIdxi < length\
-1000 <= inci <= 1000\

Thinking
-------------------
* Create a array to store the difference between adjacent elements
    * diff_arr[startInd] += increment
    * diff_arr[endInd + 1] -= increment

* To restore the array:
    * new_arr[0] = diff_arr[0]
    * new_arr[i] = new_arr[i-1] + diff_arr[i]

* Time Complexity:
    * O(k + n)
* Space Complexity:
    * O(n)
'''
from typing import List


def getModifiedArray(length: int, updates: List[List[int]]) -> List[int]:
    diff_arr = [0 for i in range(length + 1)]
    for update in updates:
        increment = update[2]
        start_index = update[0]
        end_index = update[1]

        diff_arr[start_index] += increment
        diff_arr[end_index + 1] -= increment

    # print(diff_arr)
    modified_arr = [0 for i in range(length)]
    modified_arr[0] = diff_arr[0]

    for i in range(1, length):
        modified_arr[i] = modified_arr[i-1] + diff_arr[i]
    return modified_arr


if __name__ == "__main__":
    print(getModifiedArray(5, [[1, 1, 2]]))
