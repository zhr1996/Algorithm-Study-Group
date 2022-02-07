'''
Problem
-------------------
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

* a 1-day pass is sold for costs[0] dollars,
* a 7-day pass is sold for costs[1] dollars, and
* a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

Constraints
-------------------
* 1 <= days.length <= 365
* 1 <= days[i] <= 365
* days is in strictly increasing order.
* costs.length == 3
* 1 <= costs[i] <= 1000

Thinking
-------------------
* top down
    * dp(i) is the min cost to travel start from days i

* transition
    * dp(i) = min(cost[0] + dp(i+1), cost[1] + dp[i+7], cost[2] + dp[i+30]) ,if i in travel day
        * else return dp(i+1)

* base case
    * if i > 365, return 0


'''
from typing import List
from functools import lru_cache


def mincostTickets(days: List[int], costs: List[int]) -> int:
    travel_set = set(days)

    @lru_cache
    def min_cost(i):
        # base case
        if i > 365:
            return 0

        # transition function
        if i in travel_set:
            minimum_cost = min(costs[0] + min_cost(i+1),
                               costs[1] + min_cost(i+7), costs[2] + min_cost(i+30))
            return minimum_cost
        else:
            return min_cost(i+1)
    return min_cost(1)


if __name__ == "__main__":
    print(mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
