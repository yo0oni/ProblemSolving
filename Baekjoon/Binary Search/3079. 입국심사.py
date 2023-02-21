# 친구들 총 M명
# 입국심사대 총 N개
# k번 심사대에 앉아있는 심사관의 심사 시간은 T_k
# 굳이 비어있는데 말고 더 빨리 끝나는데로 가도댐
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [int(sys.stdin.readline()) for _ in range(N)]

left = min(table)
answer = right = max(table) * M # 인원수 x 심사 소요시간 == 최대 소요시간

while left <= right:
    total = 0
    mid = (left+right) // 2
    for i in range(N):
        total += mid // table[i]
    if total >= M:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1
    # print(left, right)
print(answer)