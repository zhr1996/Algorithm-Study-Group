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
* Suppose we are very bad teachers, giving kids as little candy as possible. We would give lowest rating 1 candy, second lowest 2 candies and so on. 

* So we need to have a sorted hashmap to gradually add up the minimal candy we need (after carefully reading, this is not right)

* Check algorithm with example before writing code

* The problem says only neighbors need to get more candy ([1,0,2] only need 5 candies:[2,1,2])

* There are three kinds of numbers in the list (Equal is same with smaller)
    * smaller than both side (definitely 1)
    * smaller than one side, larger than the other (depends on the smaller side and then decide)
    * larger than both sides, waiting for both sides to decide

* Each iteraion fills at least one element ? (proof by contradiction), if all numbers are larger than both sides, impossible

* The filling sequence : 1, 2, 3. Both sides larger may be filled earlier than the one side (both sides are filled as 1). But lets just assume this sequence 

* Remember which side is smaller can help later step:
    * 2 larger than left side
    * 3 larger than right side
    # 4 larger than both sides

* Time limited error, each rank decrement by 1, need to iterate all 2 * 10^4 * 2 * 10^4

* add a funciton, check neighbor to fill, so that when filling current element also check neighbors if they can fill (aultrism algorithm)

* After adding this function, I realize by recurring calling this funciton, all type 2 and type 3 should be filled (smaller sides are getting filled, so they are filled too)

* So the last step is to fill those that are larger than both sides

Comments
-------------------
* Very interesting problem! I very much enjoyed thinking through it

'''
from typing import List
from collections import defaultdict


def candy(ratings: List[int]) -> int:
    if len(ratings) == 1:
        return 1

    candy_arr = [-1 for i in range(len(ratings))]
    type_dict = defaultdict(set)
    for i in range(len(ratings)):
        if i == 0:
            if ratings[i] <= ratings[i+1]:
                type_dict[0].add(i)
            else:
                type_dict[3].add(i)

        elif i == len(ratings) - 1:
            if ratings[i] <= ratings[i-1]:
                type_dict[0].add(i)
            else:
                type_dict[2].add(i)

        else:
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                type_dict[0].add(i)
            elif ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]:
                type_dict[4].add(i)
            else:
                if ratings[i] > ratings[i-1]:
                    type_dict[2].add(i)
                else:
                    type_dict[3].add(i)

    def check_neighbor_to_fill(index):
        if index > 0 and (index - 1) in type_dict[3]:
            candy_arr[index-1] = candy_arr[index] + 1
            check_neighbor_to_fill(index-1)

        if index < len(ratings) and (index + 1) in type_dict[2]:
            candy_arr[index+1] = candy_arr[index] + 1
            check_neighbor_to_fill(index+1)
        return

    for index in type_dict[0]:
        candy_arr[index] = 1
        check_neighbor_to_fill(index)

    for index in type_dict[4]:
        candy_arr[index] = max(candy_arr[index-1], candy_arr[index+1]) + 1

    # print(candy_arr)
    return sum(candy_arr)


if __name__ == "__main__":
    print(candy([4, 3, 5, 7]))
