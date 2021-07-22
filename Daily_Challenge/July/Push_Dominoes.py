'''
Problem
-------------------
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,\
dominoes[i] = 'R', if the ith domino has been pushed to the right, and\
dominoes[i] = '.', if the ith domino has not been pushed.\
Return a string representing the final state.\

Constraints
-------------------
n == dominoes.length\
1 <= n <= 105\
dominoes[i] is either 'L', 'R', or '.'.\

Thinking
-------------------
* Maybe do the simulation? But note here, each update should be done simultaneously, since we are considering one falling happen at the same time
    * Like a state machine
    * The end state is all the dominoes either following down, or both sides are falling dominoes
    * Maybe use a set or hashmap to store the position of each falling dominoes?
    * Comprea list after each iteratino. If no chanage, then break iteration.

* This will fail an obvious testcase, where the first dominoes is falling right. and then the rest is not falling. In this case, the time complexity will be O(n^2)

* To optimize
    * A left falling dominoe will stop falling in the following two cases:
        * met a left falling dominoe
        * one step away is a right dominoe
    * The same with right
    * As a result, we can fast forward the process by updating all the left of left falling dominoes, and updating all right of right falling dominoe
    * To make the process faster, we can use binary search
    * On of the process is wrong because we actually need to divide in half if a left falling met with a right falling

* The solution points out a better way to do this
    * Since we are only considering the adjacent symbols, we can compare symbols[0] with symbols[1], and then so on
    * Very clever !!!
'''
from typing import List


def pushDominoes(dominoes: str) -> str:
    symbols = [(i, x) for i, x in enumerate(dominoes) if x != "."]
    symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

    final_state = list(dominoes)
    for (left, x), (right, y) in zip(symbols, symbols[1:]):
        if x == y:   # 'LL' or 'RR'
            for i in range(left + 1, right):
                final_state[i] = x
        elif x == 'R' and y == 'L':
            for i in range(left + 1, right):
                if i - left == right - i:
                    final_state[i] = "."
                elif i - left < right - i:
                    final_state[i] = "R"
                else:
                    final_state[i] = "L"
    return final_state


if __name__ == "__main__":
    print(pushDominoes("..LR..L"))
