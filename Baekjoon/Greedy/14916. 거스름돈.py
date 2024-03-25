import sys
input = sys.stdin.readline

n = int(input())

flag = True
count = 0
while n > 0:
    if n % 5 == 0:
        n -= 5
    elif n % 2 == 0:
        n -= 2
    elif n > 5:
        n -= 5
    elif n > 2:
        n -= 2
    else:
        flag = False
        break
    count += 1

if flag:
    print(count)
else:
    print(-1)
