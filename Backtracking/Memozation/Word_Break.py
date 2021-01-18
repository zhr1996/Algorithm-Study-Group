# Given a string and a list of words, determine if the string can be constructed from concatenating words from the list of words. A word can be used multiple times.

# Input:

# s = "algomonster"
# words = ["algo", "monster"]
# Output: true

# Input:

# s = "aab"
# words = ["a", "c"]
# Output: false

# Backtraking try all the combinations
# any answer found then return true

# State passed to children, cur sentense that has already been spelled out
# Since a word can be used multiple times, no need to remember which word has been used

# base case, when reach the end, then return True, because all of the sentence has been spelled
# Return true, if

# Withou memo, the complexity grows with the choice of words and the length of the sentence
# For example, if there are 10 words, the sentence has 140 workds, one of the words is one character long, then there could be 10^140 possibilities
# then the complexity could be 10^10
def helper_withou_memo(s, words, index):
    if index == len(s):
        return True
    for word in words:
        if s[index:].startswith(word):
            if helper(s, words, index + len(word)):
                return True

    return False

# memoziation, keep a memo whether current status can or can't produce the final result
# memo can be used to prune the poosible state tree


def helper(s, words, index, memo):
    if index in memo:
        return memo[index]

    if index == len(s):
        return True

    for word in words:
        if s[index:].startswith(word):
            if helper(s, words, index + len(word), memo):
                return True

    memo[index] = False
    return False


def word_break(s, words):
    # WRITE YOUR BRILLIANT CODE HERE
    memo = {}
    return helper(s, words, 0, memo)


if __name__ == "__main__":
    s = input()
    words = input().split()
    if word_break(s, words):
        print('true')
    else:
        print('false')
