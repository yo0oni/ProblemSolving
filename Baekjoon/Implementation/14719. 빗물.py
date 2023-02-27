import sys
input = sys.stdin.readline

height, w = map(int, input().split())
width = list(map(int,input().split()))
count = 0

max_height = 0
max_index = 0
for i in range(w):
    if max_height < width[i]:
        max_height = width[i]
        max_index = width.index(width[i])

# 왼쪽 그룹
max_height = 0
for i in range(max_index):
    max_height = max(max_height, width[i])
    count += max_height - width[i]

# 오른쪽 그룹
max_height = 0
for i in range(len(width)-1, max_index, -1):
    max_height = max(max_height, width[i])
    count += max_height - width[i]

print(count)