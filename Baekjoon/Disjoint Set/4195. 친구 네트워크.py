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
        number[rootB] += number[rootA]
    else:
        return

n = int(input())
for _ in range(n):
    parent = dict()
    number = dict()
    net = int(input())
    for i in range(net):
        name1, name2 = map(str, input().split())

        if name1 not in parent:
            parent[name1] = name1
            number[name1] = 1

        if name2 not in parent:
            parent[name2] = name2
            number[name2] = 1
        
        union(name1, name2)
        # print(parent, number)
        print(number[find(name1)])