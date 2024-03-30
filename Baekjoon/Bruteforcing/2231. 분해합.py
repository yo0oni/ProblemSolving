import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(n):
    if i + sum(list(map(int, str(i).strip()))) == n:
        answer = i
        break

if answer == 0:
    print(0)
else:
    print(answer)