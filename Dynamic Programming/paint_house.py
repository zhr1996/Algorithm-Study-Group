'''
Problem
-------------------
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.

Constraints
-------------------
* costs.length == n
* costs[i].length == 3
* 1 <= n <= 100
* 1 <= costs[i][j] <= 20

Thinking
-------------------
* state
    * house index and prev house's color
    * we need to know prev house's color since we need it to decide the price of the rest two colors

* transition function   
    * choose a color that is different from the prev one
        * if current color is red
        * get_min_cost(i+1, prev_color=green)
        * get_min_cost(i+1, prev_color=yellow)

* base function
    * if n >= len(costs) => return 0

'''
from typing import List
from functools import lru_cache


def minCost(costs: List[List[int]]) -> int:
    @lru_cache
    def get_min_cost(index, prev_color):
        if index >= len(costs):
            return 0

        min_cost = float("inf")
        # special case, if index==0, it means this is the first house
        if index == 0:
            for i in range(3):
                min_cost = min(min_cost, costs[0]
                               [i] + get_min_cost(index+1, i))
        else:
            possible_set = set([0, 1, 2]) - set([prev_color])
            for color in possible_set:
                min_cost = min(costs[index][color] +
                               get_min_cost(index+1, color), min_cost)
        return min_cost
    return get_min_cost(0, -1)


if __name__ == "__main__":
    print(function)
