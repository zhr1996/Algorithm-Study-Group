import time

# This problem can be approaced by using difference sequence, this is one way of efficiently preserving array data when the modification is done with block
# Don't get confused about index starts at 1 and index starts at 0
# Try to think them with a real example


def arrayManipulation(n, queries):
    # arr_diff = [0 for i in range(n)]
    # faster
    arr_diff = [0] * n
    for query in queries:
        # index starts at 1
        arr_diff[query[0]-1] += query[2]
        # print(n)
        # print(query[1])
        if query[1] < n:
            arr_diff[query[1]] -= query[2]
        # print(arr_diff)
    # result_arr = [0 for i in range(n)]
    # result_arr[0] = arr_diff[0]

    # for i in range(1, n):
    #     result_arr[i] = result_arr[i-1] + arr_diff[i]
    # # print(result_arr)
    # return max(result_arr)
    result = -float("inf")
    cur = 0
    for ele in arr_diff:
        if ele < 0:
            result = max(cur, result)
        cur += ele
    result = max(result, cur)
    return result


if __name__ == '__main__':
    n = 0
    queries = []
    with open("test_maximum_sum.txt", "r") as f:
        first_line = f.readline().split()
        n = int(first_line[0])
        m = int(first_line[1])

        for _ in range(m):
            query_list = list(map(int, list(f.readline().split())))
            queries.append(query_list)
            # print(query_list)
    start_time = time.time()
    print(arrayManipulation(n, queries))
    print("--- %s seconds ---" % (time.time() - start_time))
