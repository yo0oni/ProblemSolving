import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = [0] * (N+1)

def dfs(index):
    visited[index] = True
    nodes = graph[index]
    for node in nodes:
        if not visited[node]:
            visited[node] = True
            result[node] = index
            dfs(node)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for parent in result[2:]:
    print(parent)