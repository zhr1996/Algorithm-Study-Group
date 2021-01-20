# Given a list of unique letters, find all of distinct permutations

# Thinks it like a state tree, what state would we need to determine whethere we have reached a solution
# what state would we need to determine which next state should we visit and which state should be pruned

# For the first one, we need a cur state to present letters we have chosen so far
# For the second one, we need to record which letter has been used, in this case, we can repeatedly use an array
# And for child to choose state from, we need to pass in the original input sequence too
def helper(l, used, cur, result):
    if all(used):
        result.append(cur[:])
        return
    for index, letter in enumerate(l):
        if used[index] == False:
            used[index] = True
            cur.append(letter)
            helper(l, used, cur, result)
            # Back a step
            cur.pop()
            used[index] = False
    return


def permutations(l):
    result = []
    used = [False for i in range(len(l))]
    helper(l, used, [], result)
    return result


if __name__ == "__main__":
    res = permutations(list(input()))
    print(' '.join(sorted(''.join(x) for x in res)))
