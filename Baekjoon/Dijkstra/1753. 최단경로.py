import heapq
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
start = int(input())
dist = [float('inf')] * (V+1)
dist[start] = 0

linked = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    linked[u].append((v,w))

heap = []
heapq.heappush(heap, (0, start))
    
while(heap):
    curDist, curNode = heapq.heappop(heap)
    if dist[curNode] < curDist:
        continue
        
    for toNode, toDist in linked[curNode]:
        d = curDist + toDist
        if dist[toNode] > d:
            dist[toNode] = d
            heapq.heappush(heap, (d, toNode))
            
for i in range(1, len(dist)):
    if dist[i] != float('inf'):
        print(dist[i])
    else:
        print("INF")