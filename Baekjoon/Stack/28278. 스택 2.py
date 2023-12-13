import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    number = input()

    if len(number) >= 3:
        a, b = map(int, number.split())
        stack.append(b)
        continue
    
    int_num = int(number)
    if int_num == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif int_num == 3:
        print(len(stack))
    
    elif int_num == 4:
        if stack:
            print(0)
        else:
            print(1)
    
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
