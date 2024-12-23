import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(start):
    visited = [False] * 100001
    dq = deque([(start, 0)])
    
    while dq:
        current, time = dq.popleft()
        time += 1
        
        for next in (current-1, current+1, current*2):
            if next == k:
                return time
            
            if 0 < next <= 100000 and not visited[next]:
                dq.append((next, time))
                visited[next] = True
        
if n == k:
    print(0)
else:
    print(bfs(n))