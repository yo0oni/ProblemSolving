import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
sum_ = 0

for i in range(n):
    a = int(input())

    if a == 1:
        sum_ += 1

    elif a > 0:
        plus.append(a)

    else:
        minus.append(a)

plus.sort()
minus.sort(reverse=True)

while len(plus) != 0:
    if len(plus) == 1:
        sum_ += plus.pop()

    else:
        sum_ += plus.pop() * plus.pop()

while len(minus) != 0:
    if len(minus) == 1:
        sum_ += minus.pop()

    else:
        sum_ += minus.pop() * minus.pop()

print(sum_)