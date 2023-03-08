import sys
input = sys.stdin.readline

N, L = map(int, input().split())
ant = []
for i in range(N):
    ant.append(int(input()))

sort_ant =sorted(ant,key=abs) # 절댓값순으로 정렬

leftTime = 0
for i in range(N):
    if sort_ant[i]>0: # 1, 2
        leftTime = L - sort_ant[i] # 10-1 == 9
        leftIndex = i # 2
        break

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

if leftTime>rightTime:
    print(ant.index(sort_ant[toLeft]) + 1, leftTime)

else:
    print(ant.index(sort_ant[toLeft - 1]) + 1, rightTime)