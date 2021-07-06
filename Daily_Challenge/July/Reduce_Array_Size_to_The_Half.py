'''
Problem
-------------------
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

1 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
Thinking
-------------------
* Make a hash table of all the numbers in list. Key: Number, Value: Occurence.

* Sort the hash table with the values, and then add on the values until the sum is greater or equal to half the size of the list

* Use sorted function
    * sorted(iterable, function, reverse)
'''


from typing import List
from collections import defaultdict


def minSetSize(arr: List[int]) -> int:
    occurrence_dict = defaultdict(int)
    for num in arr:
        occurrence_dict[num] += 1

    set_size = 0

    sorted_tuples = sorted(occurrence_dict.items(),
                           key=lambda x: x[1], reverse=True)
    remove_size = 0

    for item in sorted_tuples:
        remove_size += item[1]
        set_size += 1

        if remove_size >= len(arr) // 2:
            break

    return set_size


if __name__ == "__main__":
    print(minSetSize([3, 3, 3, 3]))
