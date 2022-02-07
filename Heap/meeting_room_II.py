'''
Problem
-------------------
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Constraints
-------------------
* 1 <= intervals.length <= 10^4
* 0 <= start_i < end_i <= 10^6

Thinking
-------------------
* a min-heap, storing endtime of meetings in different rooms

* the intervals in heap represents how many meeting rooms are used

* every if we need to check if a meeting room is available, we can simply check the top-most end time since this is the earlist end time

* sort the array based on start time

* Time complexity:
    * sorting: O(nlogn)
    * putting elements in: nlogn

'''
from typing import List
import heapq


def minMeetingRooms(intervals: List[List[int]]) -> int:
    heap = []
    intervals.sort()

    for interval in intervals:
        start_time, end_time = interval[0], interval[1]
        if not heap:
            heapq.heappush(heap, end_time)
            continue

        # if current interval start time is larger than the smallest end time
        # (when current meeting begins, last meeting has ended)
        # pop the last meeting out, (next meeting will use this meeting room)
        if start_time >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, end_time)

    # one meeting will only pop one meeting out, so in the end how many meetings are left in the queue is
    # how many meeting rooms we have allocated
    return len(heap)


if __name__ == "__main__":
    print(minMeetingRooms([[0, 15], [0, 30], [5, 10], [15, 20]]))
