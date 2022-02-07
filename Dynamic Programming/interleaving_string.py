'''
Problem
-------------------
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

* s = s1 + s2 + ... + sn
* t = t1 + t2 + ... + tm
* |n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Constraints
-------------------
* 0 <= s1.length, s2.length <= 100
* 0 <= s3.length <= 200
* s1, s2, and s3 consist of lowercase English letters.

Thinking
-------------------
* check if len(s1) + len(s2) == len(s3)

* top down
    * three state, index of [s3, s2, s1]
    * helper(i1, i2, i3) return if it's possible to use s1[i1:] and s2[i2:] to form s3[i3:]
    * store the sub-results

* recurrence,
    * cur = s3[i3]
    * if s1[i1] == cur, check if helper(i1+1, i2, i3+1) return True, if True, return True
        * else, if s2[i1] == cur, check if helper(i1, i2+1, i3+1) return True, if True, return True
    * else return False

* base case
    * i1 == len(s1), i2 == len(s2), i3 == len(s3), return True
    * 
'''
from typing import List


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    memory = {}
    # check length first
    if len(s1) + len(s2) != len(s3):
        return False

    def helper(i1: int, i2: int, i3: int) -> bool:
        if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
            return True

        if (i1, i2, i3) in memory:
            return memory[(i1, i2, i3)]

        cur = s3[i3]
        if i1 < len(s1) and s1[i1] == cur and helper(i1+1, i2, i3+1):
            return True

        if i2 < len(s2) and s2[i2] == cur and helper(i1, i2+1, i3+1):
            return True

        memory[(i1, i2, i3)] = False

        return False

    return helper(0, 0, 0)


if __name__ == "__main__":
    print(isInterleave("aabcc", "dbbca", "aadbbbaccc"))
