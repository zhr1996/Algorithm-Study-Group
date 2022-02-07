'''
Problem
-------------------
You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

Constraints
-------------------
* 1 <= sticks.length <= 104
* 1 <= sticks[i] <= 104

Thinking
-------------------
* keep a min heap

* heapify takes O(n) since we are not trying to sort the array, we are trying to convert it so we can get minimum efficiently

* each time pop the two smallest sticks and add their sum to cost
    * repeat until there is only one stick left

* return the total cost
'''
from typing import List
import heapq


def connectSticks(sticks: List[int]) -> int:
    heapq.heapify(sticks)

    total_cost = 0
    while len(sticks) > 1:
        stick_1 = heapq.heappop(sticks)
        stick_2 = heapq.heappop(sticks)
        total_cost += stick_1 + stick_2

        # push the combined stick to heap
        heapq.heappush(sticks, stick_1 + stick_2)

    return total_cost


if __name__ == "__main__":
    print(connectSticks([2]))
