import sys
input = sys.stdin.readline

n = int(input())
gigu = list(map(int, input().split()))
gigu.sort()

min_gigu = 0
if n % 2 != 0:
    for i in range(n // 2):
        min_gigu = max(min_gigu, gigu[i] + gigu[n-i-2])
    print(min_gigu)
else:
    for i in range(n // 2):
        min_gigu = max(min_gigu, gigu[i] + gigu[n-i-1])
    print(min_gigu)