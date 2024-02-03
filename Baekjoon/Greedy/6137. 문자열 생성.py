import sys
from collections import deque
input=sys.stdin.readline

A = int(input())
S = deque()

for i in range(A):
    S.append(input().rstrip())

T = ''
count=0
for i in range(A):
    start = 0
    end = len(S) - 1
    answer = 0
    
    while start <= end:
        if ord(S[start]) > ord(S[end]):
            answer = 0
            break
        elif ord(S[start]) < ord(S[end]):
            answer = 1
            break
        else:
            start += 1
            end -= 1

    if answer == 0:
        T += S.pop()
    elif answer == 1:
        T += S.popleft()
    count += 1
    if count % 80 == 0:
        T += '\n'

print(T)