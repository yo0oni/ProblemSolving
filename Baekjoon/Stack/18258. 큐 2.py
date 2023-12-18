import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque()

for _ in range(N):
    command = input().strip()

    if " " in command:
        comm, num = map(str, command.split())
        dq.append(num)
    
    elif not dq:
        if command == "empty":
            print(1)

        elif command == "size":
            print(0)
        
        else:
            print(-1)
            
    else:
        if command == "front":
            output = dq.popleft()
            print(output)
            dq.appendleft(output)

        elif command == "back":
            output = dq.pop()
            print(output)
            dq.append(output)

        elif command == "empty":
            print(0)

        elif command == "pop":
            print(dq.popleft())

        else:
            print(len(dq))
