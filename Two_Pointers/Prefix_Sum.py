from typing import List


def subarray_sum(arr: List[int], target: int) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    prefix_sum = {0: 0}

    # here prefix sum is the sum left of current element (current element excluded)

    cur_sum = 0

    for i, num in enumerate(arr):
        cur_sum += num
        compliment = cur_sum - target
        if compliment in prefix_sum:
            return (prefix_sum[compliment], i + 1)


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum(arr, target)
    print(' '.join(str(e) for e in res))
