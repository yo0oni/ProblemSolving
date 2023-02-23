# 탐색하려는 값 최대피
import sys
input = sys.stdin.readline

N, H_atk = map(int, input().split())
max_HP, cur_HP, damage = 0, 0, 0
for i in range(N):
    t, a, h = map(int, sys.stdin.readline().split())
    # 전쟁
    if t == 1:
        # 나 3 1, 몬스터 1 20
        check = h%H_atk
        if check == 0:
            damage = -(a * (h // H_atk - 1))
        else:
            damage = -(a * (h // H_atk))
    # 회복
    else:
        H_atk += a
        damage = h
    cur_HP += damage

    # 풀피 포션
    if cur_HP > 0:
        cur_HP = 0

    max_HP = max(max_HP, abs(cur_HP))
print(max_HP+1)
        

