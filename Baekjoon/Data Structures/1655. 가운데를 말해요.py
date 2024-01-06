import sys, heapq
input = sys.stdin.readline

max_heap = []
min_heap = []

for _ in range(int(input())):
    number = int(input())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -number)
    else:
        heapq.heappush(min_heap, number)

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        max_heap_value = -heapq.heappop(max_heap)
        min_heap_value = heapq.heappop(min_heap)

        heapq.heappush(max_heap, -min_heap_value)
        heapq.heappush(min_heap, max_heap_value)

    print((-1)*max_heap[0])