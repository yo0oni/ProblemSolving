import sys
input = sys.stdin.readline

n = int(input()) // 4

print(("long " * n).rstrip(), "int")