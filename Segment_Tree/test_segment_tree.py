def segment_tree(arr):
    segment_tree = [0 for i in range(4 * len(arr))]

    def build_tree(cur, left, right):
        if left == right:
            segment_tree[cur] = arr[left]
        else:
            mid = left + (right - left) // 2
            build_tree(cur * 2 + 1, left, mid)
            build_tree(cur * 2 + 2, mid + 1, right)
            segment_tree[cur] = segment_tree[cur * 2 + 1] + \
                segment_tree[cur * 2 + 2]

    build_tree(0, 0, len(arr) - 1)
    return segment_tree


if __name__ == "__main__":
    print(segment_tree([0, 1, 2, 3, 4]))
