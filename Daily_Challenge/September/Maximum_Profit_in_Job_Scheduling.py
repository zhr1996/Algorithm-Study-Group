'''
Problem
-------------------
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Constraints
-------------------
1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104

Thinking
-------------------
* Make a class of Job with field starttime, endtime, and profit

* Sort the array of jobs according to start time.
    * max_profit[i] = max(max_profit[j] for j in range(i) and job j doesn't conflict job i) + job_i.profit
    * max_profit[x] stores the max profit gained ends with job x

* Prove the algorithm:
    * If at step i, we don't take the max_proft[j] but takes another job with lower profit:
        * then max_profit[i]* = max_profit[k] + job_i.profit, which is smaller than max_profit[j] + job_i.profit
        * this will lead to sub optimal strategy
    * Basically, we are taking the best result of a sub problem, here the sub problem is :
        * what is the best profit we can achieve without conflicting current job?
        * To get a subproblem result like this, we need each sub solution to have a clear end state, which here means:
            * the endtime of last job, and this is why we need to set the job i is the last job at each step

* Time complexity
    * O(nlogn) to sort, O(n) to traverse the array, and in each iteartion, we do a linear search of previous results, so the time complexity is
        * O(n^2)
    * Optimize
        * stop searching when endtime is bigger than current job's start time
        * An optimize we definitely can do is to use binary search to find the last job in the array whose endtime is smaller than current job's start time
        * every time we do linear search, we are doing the same thing of finding the maximum profit job, must be some way to avoid this duplicate
            * Use another array to store the maximum profit so far. so_far_max_profit[i] = max(so_far_max_profit[j] for j in range(i))
            * Then if we find the last job that ends before current job's start time, we can use the stored array to find maximum pofict previous in O(n)
        * Time Complexity: O(nlogn)
        * Space Complexity: O(n)
'''
from typing import List
import bisect


class Job:
    def __init__(self, start_time: int, end_time: int, profit: int):
        self.start_time = start_time
        self.end_time = end_time
        self.profit = profit

    def __str__(self):
        return f"[{self.start_time}, {self.end_time}, {self.profit}]"


def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    n = len(startTime)
    jobs = []
    for i in range(n):
        jobs.append(Job(startTime[i], endTime[i], profit[i]))

    jobs.sort(key=lambda job: job.end_time)
    key_array = [job.end_time for job in jobs]

    max_profit = [-1] * n
    so_far_max_profit = [-1] * n

    def find_last_job_ends_before_cur_job(i):
        cur_key = jobs[i].start_time
        index_to_be_inserted = bisect.bisect_right(key_array, cur_key)
        # needs to minus one since now index is pointing to next job
        return index_to_be_inserted - 1

    for i in range(n):
        prev_max_profit = 0
        j = find_last_job_ends_before_cur_job(i)

        if j != -1:
            prev_max_profit = so_far_max_profit[j]

        max_profit[i] = jobs[i].profit + prev_max_profit
        if i == 0:
            so_far_max_profit[i] = max_profit[i]
        else:
            so_far_max_profit[i] = max(so_far_max_profit[i-1], max_profit[i])
    return max(max_profit)


if __name__ == "__main__":
    print(jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
