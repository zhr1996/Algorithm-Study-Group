'''
Problem
-------------------
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Constraints
-------------------
* 1 <= prices.length <= 5 * 10^4
* 1 <= prices[i] < 5 * 10^4
* 0 <= fee < 5 * 10^4

Thinking
-------------------
* state
    * day index
    * whether holding stock

* maybe we just need add the transaction fee when each time we sell a stock?

* transition
    * get_max_profit(day_index, holding_stock)
        * if not holding_stock, take max from below
            * either buy a stock: -prices[day_index] + get_max_profit(day_index+1, holding_stock=1)
            * or don't buy a stock: get_max_profit(day_index+1, holding_stock=0)
        * if holding a stock, take max from below
            * sell it. prices[day_index] - sale_tax + get_max_profit(day_index+1, holding_stock=0)
            * or don't sell it. get_max_profit(day_index+1, holding_stock=1)

* base case
    * day_index >= len(arr), return 0
'''
from typing import List
from functools import lru_cache


def maxProfit(prices: List[int], fee: int) -> int:
    # two state
    #   * day index
    #   * if holding stock
    # memory = [[-1 for j in range(2)] for i in range(len(prices))]

    @lru_cache
    def get_max_profit(day, is_holding_stock):
        if day >= len(prices):
            return 0

        # if memory[day][is_holding_stock] != -1:
        #     return memory[day][is_holding_stock]

        max_profit = 0
        if is_holding_stock == 0:
            # buy the stock
            profit_1 = -prices[day] + get_max_profit(day+1, is_holding_stock=1)

            # don't buy the stock
            profit_2 = get_max_profit(day+1, is_holding_stock=0)

            max_profit = max(profit_1, profit_2)
        else:
            # sell the stock, remember the fee
            profit_1 = prices[day] - fee + \
                get_max_profit(day+1, is_holding_stock=0)

            # don't sell the stock
            profit_2 = get_max_profit(day+1, is_holding_stock=1)

            max_profit = max(profit_1, profit_2)
        # memory[day][is_holding_stock] = max_profit
        return max_profit
    return get_max_profit(0, is_holding_stock=0)


if __name__ == "__main__":
    print(maxProfit([1, 3, 2, 8, 4, 9], 2))
