# Given a sorted array, remove dupliate item in place
def remove_duplicates(arr):
    # WRITE YOUR BRILLIANT CODE HERE
    index_new_array = 0
    index_old_array = 0
    # Two pointers, one point to the current position of the old array, one is the new array
    prev = arr[0]
    index_old_array += 1
    index_new_array += 1
    while index_old_array < len(arr):
        if arr[index_old_array] != prev:
            arr[index_new_array] = arr[index_old_array]
            prev = arr[index_old_array]
            index_new_array += 1
        index_old_array += 1
    return index_new_array


if __name__ == '__main__':
    arr = list(map(int, (input().split())))
    n = remove_duplicates(arr)
    print(' '.join(str(x) for x in arr[: n]))
