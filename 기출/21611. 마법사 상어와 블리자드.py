import sys
input = sys.stdin.readline

# N은 항상 홀수이고
# 마법사 상어는 ((N+1)/2, (N+1)/2)에 있다.
# 달팽이 회전

# 상어가 있는 칸을 제외한 나머지 칸에는 구슬이 하나 들어갈 수 있다.
# 구슬은 1번 구슬, 2번 구슬, 3번 구슬이 있다.
# 같은 번호의 구슬이 연속해서 있으면 == 연속 구슬


# di 방향으로 거리가 si 이하인 모든 칸에 있는 구슬을 모두 파괴
# 구슬이 파괴되면 그 칸은 빈 칸이 된다.


# todo
# [1] 파편 던지기
    # d, s 기준으로 얼음 던지기
    # 구슬 땡기기 -> 빈칸된 부분 메꿔야됨
# [2] 폭발
    # 4개 이상 연속하는 구슬 달팽이 회전으로 계산하기
        # 숫자 저장하다가 리스트가 4되면, 지금까지 저장한 인덱스에 0 대입
    # [1]로 이동
    # 다시 [2]
    # 불가능할 때까지 반복
# [3] 변화
    # 달팽이 회전으로 연속하는 숫자 그룹 저장
    # 하나의 그룹 데이터를 변경할 것
        # (그룹에 들어있는 구슬 개수, 그룹을 이루는 구슬 번호)
        # 뒤 튜플로 달팽이 회전 갱신
        # 만약 달팽이 크기 넘어가면 그 이후는 break

# 저장해야 할 결과
    # 폭발한 1번 구슬의 개수 * 1
    # 폭발한 2번 구슬의 개수 * 2
    # 폭발한 3번 구슬의 개수 * 3


# ↑, ↓, ←, →
# 1, 2, 3, 4
yi = [-1, 1, 0, 0]
yj = [0, 0, -1, 1]

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

# (0, 0)이 끝임
N, M = map(int, input().split())
goosle = [list(map(int, input().split())) for _ in range(N)]
blizd = [list(map(int, input().split())) for _ in range(M)]

position = []
count, flag, dr = 0, 0, 0
max_count = 1
ci, cj = N // 2, N // 2

# 달팽이 회전 탐색 포지션 저장
for t in range(N * N - 1):
    count += 1
    ci, cj = ci + di[dr], cj + dj[dr]
    position.append((ci, cj))

    if count == max_count:
        count = 0
        dr = (dr + 1) % 4

        if flag == 0:
            flag = 1
        else:
            flag = 0
            max_count += 1


def bomb(live_goosle):
    global answer

    bomb_goosle = []
    live_goosle.append(-1)
    i = 0
    while i < len(live_goosle) - 1:
        j = i + 1
        while live_goosle[i] == live_goosle[j]:
            j += 1

        if (j-i) >= 4: # 폭발
            answer += live_goosle[i] * (j - i)
        else:
            bomb_goosle += [live_goosle[i]] * (j - i)

        i = j

    live_goosle.pop()
    return bomb_goosle

answer = 0
ci, cj = N // 2, N // 2
for dr, speed in blizd:
    # 공격
    for s in range(1, speed+1):
        ni, nj = ci + yi[dr-1]*s, cj + yj[dr-1]*s
        goosle[ni][nj] = 0

    # 살아남은 구슬 확인
    live_goosle = []
    for i, j in position:
        if goosle[i][j] > 0:
            live_goosle.append(goosle[i][j])

    # 폭발
    # 살아남은 구슬 중 같은 숫자가 연속으로 4개 이상 있으면 삭제됨
    # 그리고 달팽이회전으로 다시 탐색한 후 다시 체크 (반복)
    while True:
        bomb_goosle = bomb(live_goosle)

        # 터진 후 구슬이랑 터지기 전 구슬이 같으면 == 안터진 거임
        if len(bomb_goosle) == len(live_goosle):
            break

        live_goosle = bomb_goosle

    # 변화
    trans_goosle = []
    bomb_goosle.append(-1)
    i = 0
    while i < len(bomb_goosle) -1:
        j = i + 1

        while bomb_goosle[i] == bomb_goosle[j]:
            j += 1

        trans_goosle += [(j-i), bomb_goosle[i]]
        i = j


    # 지금까지 바뀐 모든 과정을
    # 기존의 goosle에 저장
    goosle = [[0] * N for _ in range(N)]
    for i in range(min(len(trans_goosle), N*N-1)):
        goosle[position[i][0]][position[i][1]] = trans_goosle[i]

print(answer)