import sys
from collections import deque
input = sys.stdin.readline

c = int(input())
n = int(input())
computers = [[] for _ in range(c+1)]
for index in range(n):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)
    

def bfs(start):
    count = 0
    visited = [False] * (c+1)
    dq = deque([start])
    visited[1] = True
    
    while dq:
        current = dq.popleft()
        
        for next in computers[current]:
            if not visited[next]:
                visited[next] = True
                dq.append(next)
                count += 1
    
    return count

print(bfs(1))