import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ramp = []
for _ in range(n):
    ramp.append(list(map(int, input().strip())))

k = int(input())

ramp_zero_count = [0] * n
for i in range(n):
    zero_count = 0
    for j in range(m):
        if ramp[i][j] == 0:
            zero_count += 1
    ramp_zero_count[i] = zero_count

def get_count_of_same_ramp_row(i):
    count = 1
    for j in range(n):
        if i != j and ramp[i] == ramp[j]:
            count += 1
    return count

answer = 0
for i in range(n):
    if ramp_zero_count[i] <= k and ramp_zero_count[i] % 2 == k % 2:
        answer = max(answer, get_count_of_same_ramp_row(i))

print(answer)