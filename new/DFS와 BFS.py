import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
spots = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    spots[a].append(b)
    spots[b].append(a)

for i in range(len(spots)):
    spots[i].sort()

dfs_visited = [False] * (n+1)
dfs_visited[v] = True
dfs_answer = [str(v)]

def dfs(v):
    global dfs_answer
    
    if not spots[v]:
        return " ".join(dfs_answer)
        
    else:
        for cv in spots[v]:
            if not dfs_visited[cv]:
                dfs_visited[cv] = True
                dfs_answer.append(str(cv))
                dfs(cv)
    
    return " ".join(dfs_answer)

def bfs(v):
    bfs_visited = [False] * (n+1)
    bfs_visited[v] = True
    dq = deque(spots[v])
    bfs_answer = [str(v)]
    
    while dq:
        cv = dq.popleft()
        if not bfs_visited[cv]:
            bfs_answer.append(str(cv))
            bfs_visited[cv] = True
        
        
        for nv in spots[cv]:
            if not bfs_visited[nv]:
                dq.append(nv)
    
    return " ".join(bfs_answer)

print(dfs(v))
print(bfs(v))