import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        try:
            print(heapq.heappop(hq)[1])
        except:
            print(0)