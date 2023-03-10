import sys
import heapq

n = int(sys.stdin.readline())
ab = []
[heapq.heappush(ab, list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
l, p = map(int, sys.stdin.readline().split())
cnt = 0
heap = []

while p < l:

    while ab and ab[0][0] <= p:
        a, b = heapq.heappop(ab)
        heapq.heappush(heap, [-b, a])

    if not heap:
        cnt = -1
        break

    b, a = heapq.heappop(heap)
    p += -b
    cnt += 1

print(cnt)