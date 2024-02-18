import sys
input = sys.stdin.readline

n, x = map(int, input().split())
bob = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda b: (b[0] - b[1]), reverse=True)

x -= 1000 * n
answer = sum([i[1] for i in bob])

for b in bob:
    if x >= 4000 and b[0] > b[1]: # 돈이 4천원 이상 있고, A식당의 가치가 더 높으면
        answer += b[0] - b[1]
        x -= 4000
    else:
        break

print(answer)