import sys
from collections import deque
sys = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    visited = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if visited[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                visited[i] = 1
                result[x][i] = 1

for i in range(0, n):
    bfs(i)

for i in result:
    print(*i)