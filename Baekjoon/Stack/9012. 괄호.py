import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    stack = []
    strings = input().strip()

    for string in strings:
        if string == "(":
            stack.append(string)
        elif stack and string == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(string)

    if len(stack) != 0:
        print("NO")
    else:
        print("YES")