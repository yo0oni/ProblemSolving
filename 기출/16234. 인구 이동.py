import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 0

def move(union):
    union_sum = 0
    
    for x, y in union:
        union_sum += graph[x][y]

    return union_sum // len(union)


def bfs(a, b, visited):
    dq = deque([(a, b)])
    union = [(a, b)]
    visited[a][b] = True

    while dq:
        x, y = dq.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                    union.append((nx, ny))

    moved = move(union)
    for x, y in union:
        graph[x][y] = moved

    return len(union) > 1  # 인구 이동이 발생하면 True, 아니면 False


def possible():
    global count
    visited = [[False] * N for _ in range(N)]
    movement = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    movement = True
    
    if movement:
        count += 1
    return movement


graph = [list(map(int, input().split())) for _ in range(N)]

while True:
    if not possible(): 
        break

print(count)

# 모든 칸 탐색하긴 해야됨 -> 상하좌우로 -> bfs
# 이때 인구 수 조건에 부합해야 국경선 열림

# 만약 탐색이 막히면 탐색 안한 칸으로 이동해서 재탐색 시작 (대신 방문 안 한 칸으로만 탐색 시작)
# 모든 칸이 다 탐색되었으면 인구이동 시작

# 인구 이동 끝나고 방문여부 초기화
# 처음부터 다시 시작