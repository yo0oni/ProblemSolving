import sys
from collections import deque
input = sys.stdin.readline

# 유적지는 5×5
# 유물 조각은 총 7가지 종류로, 각각 숫자 1부터 7로 표현됩니다.
# 3×3 격자를 선택하여 격자를 회전
# 선택된 격자는 시계 방향으로 90도, 180도, 270도 중 하나의 각도만큼 회전

# [1] 3x3 격자 선택
    # 회전
    # (1) 유물 1차 획득 가치를 최대화하고, 그러한 방법이 여러가지인 경우
    # (2) 회전한 각도가 가장 작은 방법을 선택합니다. 그러한 경우도 여러가지인 경우
    # (3) 회전 중심 좌표의 열이 가장 작은 구간을, 그리고 열이 같다면 행이 가장 작은 구간을 선택합니다.

# [2] 유물 획득
    # 인접한 조각들이 3개 이상일 경우
    # 유물의 가치 == 조각의 개수 >= 3

# 유적의 벽면에는 1부터 7 사이의 숫자가 M개
# [3] 유물 채워넣기
    # 열 번호가 작은 순으로 조각이 생겨납니다.
    # 만약 열 번호가 같다면 행 번호가 큰 순으로 조각이 생겨납니다.

    # 유적의 벽면에 써 있는 숫자를 사용한 이후에는 다시 사용할 수 없
    # 다시 유물획득
    # 조각이 3개 이상 연결되지 않아 유물이 될 수 없을 때까지 반복됩니다.

# 총 K 번의 턴에 걸쳐 진행됩니다.
# 유물 얻을 수 없으면 중간에 즉시 종료 -> 출력 ㄴㄴ

K, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
yumul = deque(list(map(int, input().split())))

def turn(si, sj, board):
    new_board = [x[:] for x in board]
    for i in range(3):
        for j in range(3):
            new_board[si + i][sj + j] = board[si + 3 - j - 1][sj + i]
    return new_board

def bfs(board):
    dq = deque()
    visited = [[False] * 5 for _ in range(5)]
    visited[0][0] = True

    total_value = 0
    total_position = []

    for i in range(5):
        for j in range(5):
            dq.append((i, j))
            position = [(i, j)]

            while dq:
                ci, cj = dq.popleft()
                visited[ci][cj] = True

                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = ci + di, cj + dj

                    if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                        if board[ni][nj] == board[ci][cj]:
                            visited[ni][nj] = True
                            dq.append((ni, nj))
                            position.append((ni, nj))

            if len(position) >= 3:
                total_value += len(position)
                total_position += position

    return total_position, total_value

answer = []
for _ in range(K):
    max_value = 0
    total_value = 0
    value_position = []
    max_board = []

    for d in range(1, 4): # 회전
        for j in range(3):
            for i in range(3):

                new_board = [x[:] for x in board]
                for _ in range(d):
                    new_board = turn(i, j, new_board)

                position, value = bfs(new_board)
                if max_value < value:
                    max_value = value
                    value_position = position
                    max_board = new_board

    if max_value == 0:
        break

    while True:
        # answer += 최대 유물 가치
        total_value += max_value

        # 유물 지우기
        for i, j in value_position:
            max_board[i][j] = 0

        # 채워넣기
        for j in range(5):
            for i in range(4, -1, -1):
                if max_board[i][j] == 0:
                    max_board[i][j] = yumul.popleft()

        value_position, max_value = bfs(max_board)

        if max_value == 0:
            break

    answer.append(total_value)
    board = max_board

print(*answer)