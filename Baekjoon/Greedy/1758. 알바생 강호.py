import sys
input = sys.stdin.readline

n = int(input())
result = 0

tips = []
for _ in range(n):
    tips.append(int(input()))

tips.sort(reverse=True)
total_tip = 0
for index in range(0, len(tips)):
    tip = tips[index] - index
    if tip > 0:
        total_tip += tip

print(total_tip)