import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    prompt = list(input().split())

    if prompt[0] == "push":
        stack.append(prompt[1])
    elif prompt[0] == "pop":
        if stack:
            print(stack.pop(0))
        else:
            print(-1)
    elif prompt[0] == "front":
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif prompt[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif prompt[0] == "size":
        print(len(stack))
    elif prompt[0] == "back":
        if stack:
            print(stack[-1])
        else:
            print(-1)