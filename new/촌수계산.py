import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())

family = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

visited = [False] * (n+1)
def dfs(current, depth):
    global end
    
    if current == end:
        return depth

    visited[current] = True
    for next in family[current]:
        if not visited[next]:
            result = dfs(next, depth + 1)
            if result != -1:
                return result

    return -1
    
    
print(dfs(start, 0))