import sys
input = sys.stdin.readline

a, b = map(str, input().split())
print(max(a[::-1], b[::-1]))