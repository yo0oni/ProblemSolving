import sys
from collections import deque
input = sys.stdin.readline

def find_password(words):
    left, right = deque(), deque()
    cursor = 0

    for word in words:
        if word == "<" and left:
            right.appendleft(left.pop())
            cursor -= 1
        
        elif word == ">" and right:
            left.append(right.popleft())
            cursor += 1

        elif word =="-" and left:
            left.pop()
            cursor -= 1

        elif word != "<" and word != ">" and word != "-" :
            left.append(word)
        
    return ''.join(left) + ''.join(right)


n = int(input())
for _ in range(n):
    words = input().strip()
    print(find_password(words))