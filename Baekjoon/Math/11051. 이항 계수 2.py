import sys, math
input = sys.stdin.readline

N, K = map(int, input().split())
print(math.comb(N,K)%10007)