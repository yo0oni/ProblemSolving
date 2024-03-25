import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())

answer = 0
left = 1
right = m
for _ in range(j):
    where = int(input())

    while where < left or where > right:
        if where > right:
            left += 1
            right += 1
        elif where < left:
            left -= 1
            right -= 1

        answer += 1
    temp = where
    
print(answer)