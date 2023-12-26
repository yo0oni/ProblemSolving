import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = dict()
name = dict()
index = 1

for _ in range(N):
    poketmon = input().strip()
    number[index] = poketmon
    name[poketmon] = index
    index += 1

for _ in range(M):
    find = input().strip()

    if find.isdigit():
        print(number[int(find)])

    else:
        print(name[find])