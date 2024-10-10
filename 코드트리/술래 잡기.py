import sys
input = sys.stdin.readline

n, m, h, K = map(int, input().split())
domang = []
for _ in range(m):
    i, j, d = map(int, input().split())
    domang.append([i-1, j-1, d])

tree = []
for _ in range(h):
    i, j = map(int, input().split())
    tree.append((i-1, j-1))

# 달팽이 회전 코스터 저장하자
si, sj = n//2, n//2


# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
si, sj = n//2, n//2

max_count = 1
count, flag, sd, val = 0, 0, 0, 1
answer = 0
for k in range(1, K + 1):

    # [1] 도망자들 동시 움직
    for index, (i, j, dr) in enumerate(domang):
        if abs(si - i) + abs(sj - j) <= 3:
            ni, nj = i + di[dr], j + dj[dr]

            if 0 <= ni < n and 0 <= nj < n:
                if (ni, nj) != (si, sj):
                    domang[index][0], domang[index][1] = ni, nj

            else:
                domang[index][2] = (domang[index][2] + 2) % 4
                ni, nj = i + di[domang[index][2]], j + dj[domang[index][2]]
                if (ni, nj) != (si, sj):
                    domang[index][0], domang[index][1] = ni, nj

    # [2] 술래 움직
    count += 1
    si, sj = si + di[sd], sj + dj[sd]

    if (si, sj) == (0, 0):  # 안쪽으로 동작하는 달팽이
        max_count, count, flag, val = n, 1, 1, -1
        sd = 2

    elif (si, sj) == (n//2, n//2):  # 바깥으로 동작하는 달팽이
        max_count, count, flag, val = 1, 0, 0, 1
        sd = 0

    else:
        if max_count == count:
            count = 0
            sd = (sd + val) % 4

            if flag == 0:
                flag = 1

            else:
                max_count += val
                flag = 0

    siya = {(si, sj), (si + di[sd], sj + dj[sd]), (si + di[sd] * 2, sj + dj[sd] * 2)}
    for index in range(len(domang)-1, -1, -1):
        if (domang[index][0], domang[index][1]) not in tree and (domang[index][0], domang[index][1]) in siya:
            domang.pop(index)
            answer += k

    if not domang:
        break

print(answer)