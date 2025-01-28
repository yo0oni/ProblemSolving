import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    if x < y:
        parent[x] = y
    else:
        parent[y] = x


n, m = map(int, input().split())
parent = [i for i in range(n)]
answer = 0

for i in range(m):
    a, b = map(int, input().split())
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if parent_a == parent_b:
        answer = i + 1
        break
    
    else:
        union_parent(parent_a, parent_b)

print(answer)