import sys
from itertools import combinations
input = sys.stdin.readline

talls = []
for _ in range(9):
    talls.append(int(input()))

talls = list(combinations(talls, 7))

answer = []
for tall in talls:
    if sum(tall) == 100:
        answer = list(tall)

answer.sort()
for tall in answer:
    print(tall)