'''
Problem
-------------------
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints
-------------------
* 1 <= prices.length <= 10^5
* 0 <= prices[i] <= 10^4

Thinking
-------------------
* one state variable 
    * index of day
    * if currently holding a stock or not.

* max_profit(i, is_holding_stock) 
    * buy, sell, or make no change
    * if is_holding=1:
        * if sell - max_profit(i+1, 0) + prices[i]
        * if hold - max_profit(i+1, 1)
    * if is_holding=0:
        * if buy - max_profit(i+1, 1) - prices[i]
        * if don't buy - max_profit(i+1, 0)

* base case
    * if index >= len(prices), return 0
'''
from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    memory = [[-float('inf') for _ in range(2)] for _ in range(n)]

    def max_profit(i, holding_stock):
        if i >= n:
            return 0
        if memory[i][holding_stock] != -float('inf'):
            return memory[i][holding_stock]

        max_pro = -1
        if holding_stock == 1:
            # sell
            sell_pro = prices[i]
            # don't seel
            dont_sell_pro = max_profit(i+1, 1)
            max_pro = max(sell_pro, dont_sell_pro)
        else:
            # buy
            buy_pro = -prices[i] + max_profit(i+1, 1)
            # don't buy
            dont_buy_pro = max_profit(i+1, 0)
            max_pro = max(buy_pro, dont_buy_pro)
        memory[i][holding_stock] = max_pro
        return max_pro
    max_profit = max_profit(0, 0)
    return max_profit


if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))
