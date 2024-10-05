import sys
from collections import deque
input = sys.stdin.readline

# 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고,
# 스타트링크가 있는 곳의 위치는 G층이다. 
# 강호가 지금 있는 곳은 S층이고, 
# 이제 엘리베이터를 타고 G층으로 이동하려고 한다.

def bfs(s, g):
    global visited, u, d
    dq = deque([(s, 0)])
    count = 0
    
    while dq:
        current, count = dq.popleft()
        
        if current == g:
            return count
        
        if 0 < current + u <= f and not visited[current + u]:
            visited[current + u] = True
            dq.append((current + u, count + 1))
        
        if 0 < current - d <= f and not visited[current - d]:
            visited[current - d] = True
            dq.append((current - d, count + 1))
        
    return None
    

f, s, g, u, d = map(int, input().split())
visited = [False] * (f+1)

result = bfs(s, g)
if result is not None:
    print(result)
else:
    print("use the stairs")