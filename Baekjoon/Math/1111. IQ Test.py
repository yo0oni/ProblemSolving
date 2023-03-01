import sys
input = sys.stdin.readline

# y = ax + b
n = int(input())
num = list(map(int, input().split()))
print(num)

a = num[2]//num[1]