import sys
input = sys.stdin.readline

c, p = map(int, input().split())
heights = list(map(int, input().split()))

answer = 0
if p == 1:
    answer += c
    for idx in range(c-3):
        if heights[idx] == heights[idx+1] and heights[idx+1] == heights[idx+2] and heights[idx+2] == heights[idx+3]:
            answer += 1

elif p == 2:
    for idx in range(c-1):
        if heights[idx] == heights[idx+1]:
            answer += 1

elif p == 3:
    for idx in range(c-1):
        if heights[idx] == heights[idx+1] + 1:
            answer += 1
    for idx in range(c-2):
        if heights[idx] == heights[idx+1] and heights[idx+1] + 1 == heights[idx+2]:
            answer += 1

elif p == 4:
    for idx in range(c-1):
        if heights[idx] + 1 == heights[idx+1]:
            answer += 1
    for idx in range(c-2):
        if heights[idx+1] == heights[idx+2] and heights[idx] - 1 == heights[idx+1]:
            answer += 1

elif p == 5:
    for idx in range(c-1):
        if heights[idx] == heights[idx+1] + 1 or heights[idx] + 1 == heights[idx+1]:
            answer += 1
    for idx in range(c-2):
        if (heights[idx] == heights[idx+2] and heights[idx] - 1 == heights[idx+1]) or (heights[idx] == heights[idx+1] and heights[idx+1] == heights[idx+2]):
            answer += 1

elif p == 6:
    for idx in range(c-1):
        if heights[idx] == heights[idx+1] or heights[idx] - 2 == heights[idx+1]:
            answer += 1
    for idx in range(c-2):
        if (heights[idx] + 1 == heights[idx+2] and heights[idx+2] == heights[idx+1]) or (heights[idx] == heights[idx+1] and heights[idx+1] == heights[idx+2]):
            answer += 1

elif p == 7:
    for idx in range(c-1):
        if heights[idx] == heights[idx+1] or heights[idx] + 2 == heights[idx+1]:
            answer += 1
    for idx in range(c-2):
        if (heights[idx] == heights[idx+2] + 1 and heights[idx] == heights[idx+1]) or (heights[idx] == heights[idx+1] and heights[idx+1] == heights[idx+2]):
            answer += 1

print(answer)