import sys, math
input = sys.stdin.readline

M = int(input())
stones = list(map(int, input().split()))
K = int(input())

sum_color = math.comb(sum(stones), K)

case_color = 0
for index in range(M):
    case_color += math.comb(stones[index], K)

print(case_color/sum_color)