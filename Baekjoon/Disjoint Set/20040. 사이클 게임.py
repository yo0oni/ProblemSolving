import sys
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b): # 1 3
    rootA = find(a) # 2
    rootB = find(b) # 3
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

n, m = map(int,input().split())
# 0, 1, 2, 3, 4, 5
parent = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):  # 사이클 발생시
        print(i + 1)
        break
    union(a, b)
else:
    print(0)