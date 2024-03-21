import sys
input = sys.stdin.readline

total = int(input())
n = int(input())

expect = 0
for _ in range(n):
    price, count = map(int, input().split())
    expect += (price*count)

if expect == total:
    print("Yes")
else:
    print("No")