import sys
from collections import deque
input = sys.stdin.readline

# 총 f층
# 목표는 g층
# 현재는 s층

F, S, G, U, D = map(int, input().split())

min_count = float('inf')
visited = [False] * (F+1)
time = 0
def bfs(start):
    dq = deque([(start, 0)])
    
    while dq:
        current, time = dq.popleft()
        
        if current == G:
            return time
        
        for next in (current+U, current-D):
            if 0 < next <= F and not visited[next]:
                visited[next] = True
                dq.append((next, time+1))
                
    return "use the stairs"
                
    

print(bfs(S))