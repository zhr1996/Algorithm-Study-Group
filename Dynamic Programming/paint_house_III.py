'''
Problem
-------------------
There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.

Constraints
-------------------
* m == houses.length == cost.length
* n == cost[i].length
* 1 <= m <= 100
* 1 <= n <= 20
* 1 <= target <= m
* 0 <= houses[i] <= n
* 1 <= cost[i][j] <= 104

Thinking
-------------------
* dp[i][j][k] - 
    * minimum cost of having exact k neighbors with house i painted with color j

* top down 
    * start from the problem we want to solve, and gradualyy make it become smaller problems
    * min_cost(i,j,t) - paint house starting from index i, with house painted at index i - 1 color j, to exactly t neighbors
* transition
    * if house[i] != 0, we don't have a choice
    * if houses[i] == 0, we can 
        * paint in same color j as previous house, and decrement t with 1, so we are trying to solve min_cost(i + 1, j , t), and to the result add in 
          colors[i][j]
        * paint in different color, loop through all the colors, and then make the problem becomes trying to solve min_cost(i+1, k, t-1), and add to the result colors[i][k]

* base case
    * i == len(houses)
        * if t > 0, we still have neighbors to paint left, so we failed, return float('inf')
        * if t < 0, we painted too many neighbors, so we failed too, indicate by return float('inf)
        * if t == 0, we paint exactly ased neighbors, mission succeed, return 0 since we are not painting any more houses 

* what's our target
    * and to de-compose it smaller problems, what state variable do we need to keep when calling functions

* time complexity
    * O(m * n)
'''
from typing import List


def minCost(houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    dp = {}

    def min_cost(i: int, j: int, k: int) -> int:
        # base case
        if i == len(houses):
            if k == 0:
                return 0
            else:
                return float('inf')

        # trim the branch
        if k < 0:
            return float('inf')

        # check in memory
        if (i, j, k) in dp:
            return dp[(i, j, k)]

        # transition
        minimum_cost = float('inf')

        # if house is painted
        if houses[i] != 0:
            if houses[i] == j:
                minimum_cost = min_cost(i+1, j, k)
            else:
                minimum_cost = min_cost(i+1, houses[i], k-1)
        else:
            # paint in different color
            for c in range(1, n+1):
                if c == j:
                    continue
                minimum_cost = min(minimum_cost, min_cost(
                    i+1, c, k-1) + cost[i][c-1])

            if j != -1:
                # paint in same color
                minimum_cost = min(
                    minimum_cost, min_cost(i+1, j, k) + cost[i][j-1])
        dp[(i, j, k)] = minimum_cost
        return minimum_cost

    minimum_cost = min_cost(0, -1, target)
    return minimum_cost if minimum_cost != float('inf') else -1


if __name__ == "__main__":
    print(minCost([0, 2, 1, 2, 0],
                  [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3))
