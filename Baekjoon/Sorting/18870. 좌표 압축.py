import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))

sorted_l = sorted(set(l))
d = dict()

for i in range(len(set(l))):
    d[sorted_l[i]] = i

for i in range(n):
    l[i] = d[l[i]]
print(*l)