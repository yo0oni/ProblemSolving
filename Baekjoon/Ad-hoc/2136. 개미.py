import sys
input = sys.stdin.readline

N, L = map(int, input().split())
ant = []
for i in range(N):
    ant.append(int(input()))

sort_ant =sorted(ant,key=abs) # 절댓값순으로 정렬

# 가장왼쪽개미가 떨어지는 시간
leftTime = 0
for i in range(N):
    if sort_ant[i]>0: # 1, 2
        leftTime = L - sort_ant[i] # 10-1 == 9
        leftIndex = i # 2
        break

# 가장 오른쪽 개미가 떨어지는 시간
rightTime = 0
for i in range(N-1, -1, -1):
    if sort_ant[i]<0: # -3
        rightTime = sort_ant[i]*(-1) # 3
        rightIndex = i # 0
        break
toLeft = 0
for i in range(N):
    if sort_ant[i]:
        if sort_ant[i] < 0:
            toLeft += 1

# 왼쪽이 가장늦게 떨어질때
if leftTime>rightTime:
    print(ant.index(sort_ant[toLeft]) + 1, leftTime)

# 오른쪽이 가장 늦게 떨어질때
else:
    print(ant.index(sort_ant[toLeft - 1]) + 1, rightTime)