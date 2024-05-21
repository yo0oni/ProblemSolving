import sys
from collections import deque
input = sys.stdin.readline

stack = []
answer = []
n = int(input())
flag = False

push_number = 1
for _ in range(n):
    number = int(input())

    while push_number <= number:
        stack.append(push_number)
        answer.append("+")
        push_number += 1

    if stack[-1] == number:
        stack.pop()
        answer.append("-")
        
    else:
        print("NO")
        flag = True
        break

if not flag:
    for ans in answer:
        print(ans)