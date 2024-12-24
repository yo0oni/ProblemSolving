import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

def bfs(start):
    global count
    dq = deque([(start)])
    visited[start] = True
    
    while dq:
        current = dq.popleft()
        
        for next in graph[current]:
            if not visited[next]:
                dq.append(next)
                visited[next] = True


count = 0
visited = [False] * (n+1)
for number in range(1, n+1):
    if not visited[number]:
        bfs(number)
        count += 1

print(count)