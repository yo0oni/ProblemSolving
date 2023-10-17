import sys
input = sys.stdin.readline
 
N, M = map(int, input().split())
 
L = list(map(int, input().split()))
array = [0 for _ in range(N+1)]
res = [0] * M
 
for i in range(1, N+1):
    array[i] = L[i-1] + array[i-1]
    res[array[i-1] % M] += 1
 
c = res[0]
for r in res:
    c += r * (r-1) // 2

print(c)