'''
Problem
-------------------
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

1 <= n <= 2 * 10^4

Thinking
-------------------
* Use a state machine, backtracking all possible ways

* Second thought after reading the hints: dynamic programming. arr[i][j] equals to the number of ways length i ends with vowel j

* Relations:
    * dp[i+1][a] = dp[i]['e'] + dp[i]['i'] + dp[i]['u']
    * dp[i+1][e] = dp[i]['a'] + dp[i]['i']
    * dp[i+1][i] = dp[i]['e'] + dp[i]['o']
    * dp[i+1][o] = dp[i]['i']
    * dp[i+1][u] = dp[i]['o'] + dp[i]['i']

* Map:
    * 'a' : 0
    * 'e' : 1
    * 'i' : 2
    * 'o' : 3
    * 'u' : 4

'''
from typing import List


def countVowelPermutation(n: int) -> int:
    dp = [[0 for j in range(5)] for i in range(n + 1)]
    moduler = 1e9 + 7
    for j in range(5):
        dp[1][j] = 1

    for i in range(2, n + 1):
        dp[i][0] = (dp[i-1][1] + dp[i-1][4] + dp[i-1][2]) % moduler
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % moduler
        dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % moduler
        dp[i][3] = dp[i-1][2] % moduler
        dp[i][4] = (dp[i-1][3] + dp[i-1][2]) % moduler

    return int(sum(dp[n]) % moduler)


if __name__ == "__main__":
    print(countVowelPermutation(5))
