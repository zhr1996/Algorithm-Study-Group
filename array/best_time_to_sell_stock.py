# By no way a simple problem
# Actually could be dynamic programming

# Two state, min_price and max_profit_so_far

# since min price doesn't necessarily produce the best profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State
        min_price = prices[0]
        cur_max_profit = 0

        result = 0

        for price in prices:

            if price < min_price:
                result = max(result, cur_max_profit)
                min_price = price
            else:
                if price - min_price > cur_max_profit:
                    cur_max_profit = price - min_price

        result = max(result, cur_max_profit)
        return result
