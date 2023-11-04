import sys
input = sys.stdin.readline

n = int(input())

homework = []
result = [0] * 1000

for i in range(n):
    day, score = map(int, input().split())
    homework.append([day, score])

homework.sort(key=lambda x:-x[1])

for i in range(n):
    for j in range(homework[i][0]-1, -1, -1):
        if result[j] == 0:
            result[j] = homework[i][1]
            break

print(sum(result))