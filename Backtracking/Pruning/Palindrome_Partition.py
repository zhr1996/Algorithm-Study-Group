# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# Examples
# Example 1:
# Input: aab
# Output:
#   [
#   ["aa","b"],
#   ["a","a","b"]
#   ]

# Pruning: The state tree can be pruned by not considering the prefix that is not palindrome(Which is quite natural)
# Interesting thing here is I always confuse about what is the best way to check palindrome, but the very intuitive way
# is to get it by defintion, that is, reversing the original list and compare if they are the same
# And python has a really powerful way to reverse string, [::-1]

# State: current index, current partition, and the result array for storing result
# Return : Nothing

# Note partition can be viewed as combinaional search problem, because at essence, it is finding all possible combinations.

from typing import List


# Very interesting, the simplest way to check palindrome is by definition: a str same with its reverse string
def is_palindrome(s):
    return s == s[::-1]


def helper(s, index, cur, result):
    if index == len(s):
        result.append(cur[:])
        return

    # Try all prefix starts with index
    # Slicing is exclusive on the right end
    for i in range(index+1, len(s) + 1):
        prefix = s[index:i]

        if is_palindrome(prefix):
            cur.append(prefix)
            helper(s, i, cur, result)
            cur.pop()

    return


def partition(s: str) -> List[List[str]]:
    result = []
    helper(s, 0, [], result)
    return result


if __name__ == "__main__":
    result = partition(input())
    result.sort()
    for res in result:
        print(" ".join(res))
