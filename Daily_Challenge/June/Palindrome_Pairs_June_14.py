def palindromePairs(words):
    word_to_index = {}

    palindromePairsList = []
    for index, word in enumerate(words):
        word_to_index[word] = index

    for outer_index, word in enumerate(words):
        # print(word)
        # if outer_index != 0:
        #     continue
        # print(word)
        for inner_index in range(len(word)):

            s1 = word[0:inner_index]
            s2 = word[inner_index:len(word)]
            # We want to see if the reverse of either part is in the list
            # Use the dictionay above

            # If reverse of first part is present, then we need to append the reverse to the end
            # And we also need to check if the second part is palindrome or not
            # print(s1, s2)
            if s2 == s2[::-1] and s1[::-1] in word_to_index and word_to_index[s1[::-1]] != outer_index:
                if s1 == "":
                    palindromePairsList.append(
                        [word_to_index[s1[::-1]], outer_index])

                palindromePairsList.append(
                    [outer_index, word_to_index[s1[::-1]]])
            # Also for the second we have
            if s1 == s1[::-1] and s2[::-1] in word_to_index and word_to_index[s2[::-1]] != outer_index:

                # Add a case where "" exists in the word list, "" can both append to before the word or after the word

                palindromePairsList.append(
                    [word_to_index[s2[::-1]], outer_index])

    return palindromePairsList


if __name__ == "__main__":
    # print(palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
    print(palindromePairs(["aa"]))
    print(palindromePairs(["aba", ""]))
    print(palindromePairs(["ab", "ba", ""]))
