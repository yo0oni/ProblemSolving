import sys
from collections import deque
input = sys.stdin.readline

# dfs
def dfs(v):
    dfs_visit_list[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
       if dfs_visit_list[i] == 0 and graph[v][i]:
          dfs(i)

# bfs
def bfs(v):
    dq = deque()
    dq.append(v)   
    bfs_visit_list[v] = 1
    while dq:
        v = dq.popleft()
        print(v, end = " ")
        for i in range(1, n + 1):
            if bfs_visit_list[i] == 0 and graph[v][i] == 1:
                dq.append(i)
                bfs_visit_list[i] = 1
   
n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
bfs_visit_list = [0] * (n + 1)
dfs_visit_list = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1 # 연결해주기

dfs(v)
print()
bfs(v)