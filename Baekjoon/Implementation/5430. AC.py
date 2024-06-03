import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    numbers = deque(eval(input()))
    rotate = False
    fail = False

    for command in p:

        if len(numbers) <= 0 and command == "D":
            fail = True
            print("error")
            break

        if command == "R" and not rotate:
            rotate = True
        
        elif command == "R" and rotate:
            rotate = False

        elif numbers and command == "D" and rotate:
            numbers.pop()
        
        elif numbers and command == "D" and not rotate:
            numbers.popleft()


    if not fail:
        if len(numbers) == 0:
            print("[]")
            continue
        result = ""
        result += ("[")
        if rotate:
            strs = list(map(str, numbers))
            result += (",".join(strs[::-1]))
        else:
            result += (",".join(map(str, numbers)))

        result += ("]")

        print(result)