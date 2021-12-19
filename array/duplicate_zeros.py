'''
Problem
-------------------
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Constraints
-------------------
* 1 <= arr.length <= 104
* 0 <= arr[i] <= 9

Thinking
-------------------
* Think about after duplicating the elements, we will then trim some numbers

* If we know how many numbers we are going to trim. we can know what would be last num of the new array
    * Start from the end, and then count back

* Edge case
    * A zero it self may not be trimmed, but its duplicate may get trimmed
'''
from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    trim_count = 0
    for num in arr:
        if num == 0:
            trim_count += 1

    edge_zero = False
    end = len(arr) - 1
    while trim_count > 0:
        if arr[end] != 0:
            trim_count -= 1
        else:
            # if there are still 2 count left, this zero can be trimmed completely
            if trim_count >= 2:
                trim_count -= 2
            else:
                trim_count -= 1
                edge_zero = True
                break
        end -= 1

    new_end = len(arr) - 1
    while end >= 0:
        if arr[end] != 0:
            arr[new_end] = arr[end]
            new_end -= 1
        else:
            if new_end == len(arr) - 1 and edge_zero:
                arr[new_end] = 0
                new_end -= 1
            else:
                arr[new_end] = 0
                arr[new_end-1] = 0
                new_end -= 2
        end -= 1
    return


if __name__ == "__main__":
    input = [1, 0, 2, 3, 0, 4, 5, 0]
    print(input)
    print(duplicateZeros(input))
    print(input)
