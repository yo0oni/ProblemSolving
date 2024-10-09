from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

movement = deque()
for _ in range(M):
    d, s = map(int, input().split())
    movement.append([d-1, s])

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

groom = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
visited = [[False] * N for _ in range(N)]
for dir, speed in movement:
    # 구름 이동
    new_groom = []

    for gi, gj in groom:
        ni, nj = (gi + di[dir]*speed) % N, (gj + dj[dir]*speed) % N
        board[ni][nj] += 1
        new_groom.append((ni, nj))

    visited = [[False] * N for _ in range(N)]
    for gi, gj in new_groom:
        visited[gi][gj] = True
        count = 0

        for d in (1, 3, 5, 7):
            ni, nj = gi + di[d], gj + dj[d]


            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] != 0:
                    count += 1

        board[gi][gj] += count # 물이 있는 대각선 칸만큼 더함

    groom = deque()
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not visited[i][j]:
                board[i][j] -= 2
                groom.append((i, j))

answer = 0
for i in range(N):
    for j in range(N):
        answer += board[i][j]

print(answer)
