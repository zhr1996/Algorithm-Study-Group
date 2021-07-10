'''
Problem
-------------------
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse 
of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). 
For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s containing digits and the '*' character, return the number of ways to decode it.

Since the answer may be very large, return it modulo 109 + 7.



Constraints
-------------------
1 <= s.length <= 105
s[i] is a digit or '*'.

Thinking
-------------------
* Brute force. Backtracking for all possible combinations and mappings.

* Since brute force increase ways by one each time and the problem states that the final should module 10^9 + 7, so brute force will definitelly exceeds time criteria(runs more than 10^9 + 7)


* Dynamic Programming. Use a dp array to store the sub result. dp[i:] stores the ways to decode nums[i:]
    * So we can build up our result by dp[i:] = 
        * + dp[i + 1:], if nums[i] in key set, 
        * + dp[i + 2:], if nums[i:i+1] in key set

* Note here, when finding a valid pattern, we should multiply with the ways of decoding the rest, not add to them. 

* For wild card:
    * If nums[i] == "*", then multiply dp[i+1] with 9
    * If nums[i:i+1] == "1*", then multiply dp[i+2] with 9
    * If nums[i:i+1] == "2*", then multiply dp[i+2] with 6
    * If nums[i:i+1] == "*1", then multiply dp[i+2] with 2
    * If nums[i:i+1] == "*2", then multiply dp[i+2] with 2
    * ... If nums[i:i+1] == "*6", multiply dp[i+2] with 2. (11,21,12,22,...16,26 are valid)
    * start from 7, if nums[i:i+1] == "*7", multiply dp[i+2] with 1. (17, 18, 19 is valid)

* Note the corner cases: "*0"
'''
from typing import List


def numDecodings(s: str) -> int:
    dp = [0 for x in range(len(s) + 2)]
    # Initialize the end of array to 1
    dp[len(s)] = dp[len(s) + 1] = 1
    decode_ways_mapping = {}
    for i in range(1, 27):
        decode_ways_mapping[str(i)] = 1
    decode_ways_mapping['*'] = 9
    decode_ways_mapping['1*'] = 9
    decode_ways_mapping['2*'] = 6
    decode_ways_mapping['**'] = 15
    for i in range(0, 7):
        decode_ways_mapping['*' + str(i)] = 2
    for i in range(7, 10):
        decode_ways_mapping['*' + str(i)] = 1

    for i in range(len(s) - 1, -1, -1):
        if s[i] in decode_ways_mapping:
            dp[i] += decode_ways_mapping[s[i]] * dp[i+1]
            dp[i] %= 1e9 + 7
        if i < len(s) - 1 and s[i:i+2] in decode_ways_mapping:
            dp[i] += decode_ways_mapping[s[i:i+2]] * dp[i+2]
            dp[i] %= 1e9 + 7
    return int(dp[0])


if __name__ == "__main__":
    print(numDecodings("*0"))
