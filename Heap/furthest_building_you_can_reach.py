'''
Problem
-------------------
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Constraints
-------------------
* 1 <= heights.length <= 105
* 1 <= heights[i] <= 106
* 0 <= bricks <= 109
* 0 <= ladders <= heights.length

Thinking
-------------------
* if we take all the jump and we look back, we will know the ladder will always be put in the largest jumps (optimal way)
    * use bricks to fill in the small jumps
* what we could do is allocating the ladders first for the jumps we found 
    * as we move along, we replace the ladder with bricks if we found later larger jump
    * we go forward until we don't have enough bricks or we reach the end
* since we konw each time we will compare with the smallest jump that ladder is used, we can use a min-heap
'''
from typing import List
import heapq


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    min_heap = []
    i = 0
    while i < len(heights) - 1:
        if heights[i+1] > heights[i]:
            # needs a jump
            if len(min_heap) < ladders:
                # still have ladders to use
                heapq.heappush(min_heap, heights[i+1] - heights[i])
            else:
                # needs to compare to see if current jump is larger than the previous
                cur_jump = heights[i+1] - heights[i]
                if min_heap and cur_jump > min_heap[0]:
                    prev_jump = heapq.heappop(min_heap)
                    # use bricks for previous jump
                    bricks -= prev_jump
                    heapq.heappush(min_heap, cur_jump)
                else:
                    bricks -= cur_jump
        if bricks < 0:
            break
        i += 1
    return i


if __name__ == "__main__":
    print(furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 0))
