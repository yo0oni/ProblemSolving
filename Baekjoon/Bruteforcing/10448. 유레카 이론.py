import sys
input = sys.stdin.readline

answer = [0] * 1001
triangleNum = []
for i in range(1, 45):
    triangleNum.append(i * (i + 1) // 2)

for one in triangleNum:
    for two in triangleNum:
        for three in triangleNum:
            if one + two + three <= 1000:
                answer[one + two + three] = 1

t = int(input())
k = []
for _ in range(t):
    k.append(int(input()))

for target in k:
    print(answer[target])