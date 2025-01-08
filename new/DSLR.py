import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, want):
    visited = [False for _ in range(100001)]
    dq = deque([(start, "")])
    visited[start] = True
    
    while dq:
        current, answer = dq.popleft()
        
        if current == want:
            return answer
        
        d = (current*2) % 10000
        if not visited[d]:
            visited[d] = True
            dq.append((d, answer+"D"))
        
        s = (current-1) % 10000
        if not visited[s]:
            visited[s] = True
            dq.append((s, answer+"S"))
        
        l = current // 1000 + (current % 1000) * 10
        if not visited[l]:
            visited[l] = True
            dq.append((l, answer+"L"))
        
        r = current // 10 + (current % 10) * 1000
        if not visited[r]:
            visited[r] = True
            dq.append((r, answer+"R"))
        
    return answer
        

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))