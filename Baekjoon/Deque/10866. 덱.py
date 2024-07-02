import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
numbers = deque()

def push_front(x):
    numbers.appendleft(x)

def push_back(x):
    numbers.append(x)

def pop_front():
    if not numbers:
        return -1
    return numbers.popleft()

def pop_back():
    if not numbers:
        return -1
    return numbers.pop()

def size():
    return len(numbers)

def empty():
    if numbers:
        return 0
    return 1

def front():
    if not numbers:
        return -1
    return numbers[0]

def back():
    if not numbers:
        return -1
    return numbers[-1]


for _ in range(n):
    command = list(input().split())

    if command[0] == "push_front":
        push_front(command[1])

    elif command[0] == "push_back":
        push_back(command[1])

    elif command[0] == "pop_front":
        print(pop_front())

    elif command[0] == "pop_back":
        print(pop_back())

    elif command[0] == "size":
        print(size())

    elif command[0] == "empty":
        print(empty())

    elif command[0] == "front":
        print(front())

    elif command[0] == "back":
        print(back())
