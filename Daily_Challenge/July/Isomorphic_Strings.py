'''
Problem
-------------------
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Constraints
-------------------
1 <= s.length <= 5 * 104\
t.length == s.length\
s and t consist of any valid ascii character.\

Thinking
-------------------
* Make a dictionary storing the mapping between s and t

* Note: this is a one-to-one mapping, we need to check whethere the letter in t has been mapped or not
'''
from typing import List


def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    letter_mapping = {}
    letter_mapped = set()
    for i in range(len(s)):
        if s[i] not in letter_mapping:
            if t[i] in letter_mapped:
                return False
            letter_mapping[s[i]] = t[i]
            letter_mapped.add(t[i])
        else:
            if letter_mapping[s[i]] != t[i]:
                return False

    return True


if __name__ == "__main__":
    print(isIsomorphic("egf", "aff"))
