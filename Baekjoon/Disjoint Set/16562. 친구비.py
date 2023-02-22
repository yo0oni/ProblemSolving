import sys
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if money[rootA] < money[rootB]:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

n, m, k = map(int, input().split())
money =[0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]
result = 0

for i in range(m):
    friend1, friend2 = map(int, input().split())
    union(friend1, friend2)

set_ = set()
result = 0
for i in range(1, n + 1):
    if find(i) not in set_:
        print(find(i), parent, money)
        result += money[parent[i]]
        set_.add(parent[i])

if result > k:
        print("Oh no")
else:
       print(result)