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
    if rootA != rootB:
        parent[rootA] = rootB
    else:
        return

n = int(input()) # 도시의 수
m = int(input()) # 여행 계획에 속한 도시들의 수
parent = [i for i in range(n+1)]

for i in range(1, n+1): # 0, 1, 2
    cities = list(map(int, input().split()))
    # 0 1 0
    for j in range(len(cities)): # 0, 1, 2
        idx = j+1
        if cities[j] == 1:
            union(i, idx)

route = list(map(int, input().split()))
result = set()

for i in route:
    result.add(find(i))
if len(result) == 1:
    print("YES")
else:
    print("NO")