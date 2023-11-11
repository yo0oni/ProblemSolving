import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
time = [float('inf')] * (N+1)

linked = [[] for _ in range(N+1)]

for i in range(M):
    u, v, w = map(int, input().split())
    linked[u].append((v,w))

start, end = map(int, input().split())

heap = []
heapq.heappush(heap, (0, start))

while(heap):
    curTime, curNode = heapq.heappop(heap)
    if time[curNode] < curTime:
        continue
        
    for toNode, toTime in linked[curNode]:
        t = curTime + toTime
        if time[toNode] > t:
            time[toNode] = t
            heapq.heappush(heap, (t, toNode))
            
print(time[end])