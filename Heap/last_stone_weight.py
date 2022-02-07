'''
Problem
-------------------
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Constraints
-------------------
* 1 <= stones.length <= 30
* 1 <= stones[i] <= 1000

Thinking
-------------------
* heapy the array O(N)
'''
from typing import List
import heapq


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapq.heapify(stones)
    while stones:
        if len(stones) == 1:
            return -stones[0]

        largest = -heapq.heappop(stones)
        second = -heapq.heappop(stones)

        after_smash = largest - second
        if after_smash != 0:
            heapq.heappush(stones, -after_smash)

    return 0


if __name__ == "__main__":
    print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
