import sys
from collections import deque
input = sys.stdin.readline

# 1. 물통 A, B, C가 있는데 C는 이미 가득 차있음. A, B는 비어있음
# 2. 물통에 들어있는 물은 마음대로 옮길 수 이씀
# 3. 최종적으로, A의 물통이 비어있을 때 C 안에 담겨있을 수 있는 물의 양을 구하자

# A물통이 비어있을 때 C물통의 양을 구하자 -> 완전탐색 필요 BFS

def check_visited(x, y):
    global visited
    if not visited[x][y]:
        visited[x][y] = True
        dq.append((x, y))

def bfs():
    dq.append((0, 0))
    visited[0][0] = True
    
    while dq:
        x, y = dq.popleft()
        z = C - x - y # C 잔여량은 A와 B의 물량으로 결정됨!!! 이때 A는 빈 물통이여야 result

        if x == 0:
            result.append(z)

        if x > 0 and y < B:
            water = min(x, B-y)
            check_visited(x-water, y+water) # A에 담겨있던 물을 B로 이동

        if x > 0 and z < C:
            water = min(x, C-z)
            check_visited(x-water, y)

        if y > 0 and x < A:
            water = min(y, A-x)
            check_visited(x+water, y-water)

        if y > 0 and z < C:
            water = min(y, C-z)
            check_visited(x, y-water)

        if z > 0 and x < A:
            water = min(z, A-x)
            check_visited(x+water, y)

        if z > 0 and y < B:
            water = min(z, B-y)
            check_visited(x, y+water)


A, B, C = map(int, input().split())
visited = [[False] * (B+1) for _ in range(A+1)]
result = []

dq = deque()
bfs()

result.sort()
print(*result)