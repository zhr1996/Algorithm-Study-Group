'''
Problem
-------------------
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.

Constraints
-------------------
* costs.length == n
* costs[i].length == k
* 1 <= n <= 100
* 2 <= k <= 20
* 1 <= costs[i][j] <= 20

Thinking
-------------------
* the same with paint house I. use lru_cache so we don't need to explicitly specify the dimension of memory

* even if we need, we can just get the dimension(k) by looking at the length of single element in costs
'''
from typing import List
from functools import lru_cache


def minCostII(costs: List[List[int]]) -> int:
    @lru_cache
    def get_min_cost(index, prev_color):
        # base case
        if index >= len(costs):
            return 0

        # if index == 0, try all k ways
        min_cost = float("inf")
        if index == 0:
            for i in range(len(costs[index])):
                min_cost = min(
                    min_cost, costs[index][i] + get_min_cost(index+1, i))
        else:
            for i in range(len(costs[index])):
                if i == prev_color:
                    continue
                min_cost = min(
                    min_cost, costs[index][i] + get_min_cost(index+1, i))
        return min_cost
    return get_min_cost(0, -1)


if __name__ == "__main__":
    print(minCostII([[1, 3], [2, 4]]))
