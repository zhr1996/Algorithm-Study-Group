'''
Problem
-------------------
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Constraints
-------------------
1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.


Thinking
-------------------
* store frequency in a dictionary and sort the items()
'''
from typing import DefaultDict, List


def frequencySort(s: str) -> str:
    frequency_dict = DefaultDict(int)
    for i in range(len(s)):
        frequency_dict[s[i]] += 1

    sorted_item = sorted(frequency_dict.items(), key=lambda x: -x[1])

    result = []
    for letter, frequency in sorted_item:
        for i in range(frequency):
            result.append(letter)
    return "".join(result)


if __name__ == "__main__":
    print(frequencySort("cAcacbb"))
