import sys
from collections import deque
input = sys.stdin.readline

n = input()
m = int(input())
cursor = len(n)
left, right = deque(list(n.strip())), deque()

for _ in range(m):
    command = list(map(str, input().split()))
    if command[0] == "L" and left:
        cursor -= 1
        right.appendleft(left.pop())
    
    elif command[0] == "D" and right:
        left.append(right.popleft())
        cursor += 1
    
    elif command[0] == "B" and left:
        left.pop()
        cursor -= 1

    elif command[0] == "P":
        left.append(command[1])
        cursor += 1

print(''.join(left) + ''.join(right))