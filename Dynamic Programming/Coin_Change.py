from typing import List
# Sequence problem

# You are given coins of different denominations and a total amount of money. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1

# Sequence problem
# For a particular amount num, there are different subproblems: num - coints[0]. num - coins[1], ...
# then there is the sub problem
# dp[i] = min(dp[changes] + 1 for changes in [dp - coins[0], dp - coins[1], dp - coins[2])


def coinChange(coins: List[int], amount: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    SYS_MAX = float('inf')
    if amount == 0:
        return 0
    # Note here array should be declared as for x in range(amount + 1)
    dp = [SYS_MAX for x in range(amount + 1)]
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[-1] == SYS_MAX:
        return -1
    return dp[-1]


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    amount = int(input())
    print(coinChange(numbers, amount))
