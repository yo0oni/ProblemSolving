import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))
drinks.sort(reverse=True)

answer = drinks[0]
for drink in drinks[1:]:
    answer += (drink / 2)
print(answer)