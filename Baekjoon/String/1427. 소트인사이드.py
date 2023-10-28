import sys
input = sys.stdin.readline

arr = list(map(int, input().strip()))
arr.sort(reverse=True)

for str in arr:
    print(str, end='')