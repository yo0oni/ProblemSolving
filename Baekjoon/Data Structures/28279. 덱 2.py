import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

dq = deque()
for i in range(n):
    num = list(map(int, input().split()))
    l = len(dq)
    
    if num[0] == 1:
        dq.appendleft(num[1])
    elif num[0] == 2:
        dq.append(num[1])
    elif num[0] == 3:
        print(dq.popleft() if l else -1)
    elif num[0] == 4:
        print(dq.pop() if l else -1)
    elif num[0] == 5:
        print(len(dq))
    elif num[0] == 6:
        print(0 if l else 1)
    elif num[0] == 7:
        print(dq[0] if l else -1)
    elif num[0] == 8:
        print(dq[-1] if l else -1)