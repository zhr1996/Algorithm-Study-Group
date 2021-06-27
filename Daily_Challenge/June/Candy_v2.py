'''
Problem
-------------------
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104

Thinking
-------------------
* Another solution:
    * One iteration from left to right, make sure each right person gets 1 more than left person, if rating is higher, so that people would be happy when looking at left

    * Now add another iteration to maker sure people are also happy when looking from right to left, if their rating is higher than right, make their candy current amount of right amount + 1
      whichever is larger

    * Now both directions are happy!
'''
