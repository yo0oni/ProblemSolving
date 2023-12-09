import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    stack = []
    brackets = input()
    
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)

        elif bracket == ")":
            if stack and stack[-1] == "(":
                stack.pop()

            else:
                stack.append(bracket)
                
    if len(stack) != 0:
        print("NO")

    else:
        print("YES")