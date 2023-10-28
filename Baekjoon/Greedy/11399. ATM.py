import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
time = 0
sum = 0

for num in arr:
    time += num
    sum += time

print(sum)