'''
Problem
-------------------
order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Constraints
-------------------
order has length at most 26, and no character is repeated in order.\
str has length at most 200.\
order and str consist of lowercase letters only.\

Thinking
-------------------
* Create a hashmap storing all letters and its occurrence. 

* Create a priority queue for the order string. Each item in priority queue is a key-value pair, key is the letter and value is its order.

* Pop out of queue one pair at a time and check if the key exists in the hashmap. If it is, then add all occurrences to the result string.

* Add in all othere keys in the map

* Time complexity: O(n + k)
* Note: to customize compare funcitons in heapq, store key value pair as tuples and make sure the key can be compared in python.
'''
from typing import List
import heapq
from collections import defaultdict


def customSortString(order: str, str: str) -> str:
    str_letter_mapping = defaultdict(int)
    priority_queue = []
    ordered_string_arr = []
    for s in str:
        str_letter_mapping[s] += 1
    for i, letter in enumerate(order):
        heapq.heappush(priority_queue, (i, letter))

    while len(priority_queue) != 0:
        _, letter = heapq.heappop(priority_queue)
        if letter in str_letter_mapping:
            ordered_string_arr.append(letter * str_letter_mapping[letter])
            str_letter_mapping.pop(letter)

    if len(str_letter_mapping) != 0:
        for letter in str_letter_mapping:
            ordered_string_arr.append(letter * str_letter_mapping[letter])

    return "".join(ordered_string_arr)


if __name__ == "__main__":
    print(customSortString("cba", "abcd"))
