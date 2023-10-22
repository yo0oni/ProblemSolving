import sys
input = sys.stdin.readline

n, h = map(int, input().split())
suck = [0] * (h + 1) # 석순
jong = [0] * (h + 1) # 종유석

min_count = n 
range_count = 0 

for i in range(n):
    if i % 2 == 0:
        suck[int(input())] += 1
    else:
        jong[int(input())] += 1

for i in range(h - 1, 0, -1):
    suck[i] += suck[i + 1]
    jong[i] += jong[i + 1]

for i in range(1, h + 1):
    if min_count > (suck[i] + jong[h - i + 1]):
        min_count = (suck[i] + jong[h - i + 1])
        range_count = 1
    elif min_count == (suck[i] + jong[h - i + 1]):
        range_count += 1

print(min_count, range_count)