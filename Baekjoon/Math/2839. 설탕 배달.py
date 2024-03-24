import sys
input = sys.stdin.readline

n = int(input())

count = 0
while n:
    if n % 5 == 0:
        n -= 5
        count += 1
    elif n % 3 == 0:
        n -= 3
        count += 1
    elif n >= 5:
        n -= 5
        count += 1
    elif n >= 3:
        n -= 3
        count += 1
    else:
        break

if n == 0:
    print(count)
else:
    print(-1)