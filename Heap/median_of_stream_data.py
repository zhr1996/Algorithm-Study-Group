import heapq


class MedianOfStream:
    # Two heaps, one is max heap, one is min heap.
    # if two heaps have even length, take the top and take average
    # if not, take the top element on max heap
    # always balance two heaps after adding number (make sure two heaps have only one difference in length and max always larger or equal to small heap)

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_number(self, num: float) -> None:
        def __balance():
            if len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            if len(self.max_heap) > len(self.min_heap) + 1:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.min_heap) == 0 or num < self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        __balance()

    def get_median(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + (-self.max_heap[0])) / 2
        else:
            return -self.max_heap[0]


if __name__ == '__main__':
    median_of_stream = MedianOfStream()
    n = int(input())
    for _ in range(n):
        line = input().strip()
        if line == 'get':
            median = median_of_stream.get_median()
            print(f'{median:.1f}')
        else:
            num = float(line)
            median_of_stream.add_number(num)
