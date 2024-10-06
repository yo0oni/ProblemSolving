from collections import deque

n, k = map(int, input().split())
time = 0


def bfs(n):
    dq = deque()
    dq.append((n, 0))
    
    visited = [False for _ in range(100001)]
    visited[n] = True
    
    while dq:
        current, time = dq.popleft()
        
        if current == k:
            return time
        
        for next in (current + 1, current - 1, current * 2):
            if 0 <= next <= 100000 and not visited[next]:
                dq.append((next, time + 1))
                visited[next] = True

    return time

print(bfs(n))