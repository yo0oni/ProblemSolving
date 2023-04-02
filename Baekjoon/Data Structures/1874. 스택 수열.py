import sys

n = int(sys.stdin.readline())

stack = []
c_list = []

for _ in range(n):
    tmp = int(sys.stdin.readline())
    for i in range(1, tmp+1):
        if i not in stack and i not in c_list:
            stack.append(i)
            print('+')
    c_list.append(stack.pop())
    print('-')