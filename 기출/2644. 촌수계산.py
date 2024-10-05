import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    global family
    visited = [False] * (n+1)
    
    dq = deque([(a, 0)])
    visited[a] = True
    
    while dq:
        current, count = dq.popleft()
        
        if current == b:
            return count
        
        for index in range(1, n+1):
            if not visited[index] and family[current][index] == 1:
                visited[index] = True
                dq.append((index, count + 1))
                
    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())
family = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    family[x][y] = family[y][x] = 1

print(bfs(a, b))