from collections import deque

def bfs(v):
    global graph, bfs_visited
    
    dq = deque([v])
    bfs_visited[v] = True
    
    while dq:
        current = dq.popleft()
        print(current, end=" ")
        
        for index in range(1, n+1):
            if not bfs_visited[index] and graph[current][index] == 1:
                dq.append(index)
                bfs_visited[index] = True

def dfs(v):
    global graph, dfs_visited
    dfs_visited[v] = True
    print(v, end=" ")
    
    for index in range(1, n+1):
        if not dfs_visited[index] and graph[v][index] == 1:
            dfs(index)

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)