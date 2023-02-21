import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
     
def find(a):
    if a == parent[a]: # 자기 자신이 루트 노드이면 a 반환
        return a
    temp = find(parent[a]) # a의 루트 노드 찾기
    parent[a] = temp # 부모 테이블 갱신
    return parent[a]

def union(a, b):
    rootA = find(a) # 3
    rootB = find(b) # 2
    if rootA != rootB:
        parent[rootA] = rootB
    else:
        return

def check(a, b):
    if find(a) == find(b):
        return "YES"
    else:
        return "NO"

n, m = map(int, input().split())
parent = dict()

# 초기화
parent = [i for i in range(n + 1)]

for i in range(m):
    number, a, b = map(int, input().split())

    # union
    if number == 0:
        union(a, b)
    #find
    else:
        print(check(a, b))