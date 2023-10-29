import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for idx in graph[node]:
            if not visited[idx]:
                visited[idx] = True
                queue.append(idx)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
count = 0

for index in range(1, N + 1):
    if not visited[index]:
        if not graph[index]:
            count += 1
            visited[index] = True
        else:
            bfs(index)
            count += 1

print(count)