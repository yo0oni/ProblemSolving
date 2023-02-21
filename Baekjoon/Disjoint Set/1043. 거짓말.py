import sys
input = sys.stdin.readline

n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []

# 파티 개수
for _ in range(m):
    parties.append(set(input().split()[1:]))
# print(parties)

for _ in range(m):
    for party in parties:
        if party & knowList: # 교집합에 1이 있으면 진실을 아는 사람 있
            knowList = knowList.union(party)
            # 해당 파티에 참석한 모두가 진실을 알게댐

cnt = 0
for party in parties:
    if party & knowList:
        continue
    cnt += 1 # 진실을 아는 사람이 없으면 과장 ok

print(cnt)
