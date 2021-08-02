'''
Problem
-------------------
For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:

For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].

Given n, return any beautiful array nums.  (It is guaranteed that one exists.)

Constraints
-------------------
1 <= n <= 1000

Thinking
-------------------

'''
from typing import List
def beautifulArray(n: int) -> List[int]:


if __name__ == "__main__":
    print(beautifulArray(4))
