from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    visited[i][j] = True
    slst = [(i, j)]

    while dq:
        ci, cj = dq.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if board[ni][nj] == board[ci][cj]: # 같으면
                    visited[ni][nj] = True
                    dq.append((ni, nj))
                    slst.append((ni, nj))

    return slst


answer = 0
# [1] 그룹 만들기
for idx in range(4):
    group = []
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group.append(bfs(i, j))

    # [2] 조화로움 결정하기
    # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) x 그룹 a 숫자 x 그룹 b 숫자
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            count = 0

            for gi, gj in group[i]:
                for d in range(4):
                    ni, nj = gi + di[d], gj + dj[d]

                    if 0 <= ni < n and 0 <= nj < n:
                        if (ni, nj) in group[j]:
                            count += 1

            johwa = (len(group[i]) + len(group[j])) * board[group[i][0][0]][group[i][0][1]] * board[group[j][0][0]][group[j][0][1]] * count
            answer += johwa

    if idx == 3:
        break

    # [3-1]. 십자가 회전
    m = n // 2
    nboard = [[0] * n for _ in range(n)]
    nboard[m][m] = board[m][m] # 중앙은 똑같음
    for i in range(n):
        nboard[m][i] = board[i][m]
    for j in range(n):
        nboard[j][m] = board[m][n-j-1]

    # [3-3]. 사각형 4개 회전
    for i in range(m):
        for j in range(m):
            nboard[i][m-j-1] = board[j][i]

    for i in range(m):
        for j in range(m):
            nboard[i][m+1+m-j-1] = board[j][m+1+i]

    for i in range(m):
        for j in range(m):
            nboard[m+1+i][m-j-1] = board[m+1+j][i]

    for i in range(m):
        for j in range(m):
            nboard[m+1+i][m+1+m-j-1] = board[m+1+j][m+1+i]

    board = nboard

print(answer)
