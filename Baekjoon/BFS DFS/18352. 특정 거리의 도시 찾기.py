import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
road = [[] for _ in range(N+1)]

distance = [0] * (N+1)
visited = [False] * (N+1)
result = []

for _ in range(M):
    a, b = map(int, input().split())
    road[a].append(b)

def bfs(X, K):
    dq = deque([X])
    visited[X] = True
    while dq:
        city = dq.popleft()

        for i in road[city]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True
                distance[i] = distance[city] + 1
                
                if distance[i] == K:
                    result.append(i)
                    
bfs(X, K)

if len(result) == 0:
    print(-1)

else:
    result.sort()
    for i in result:
        print(i)