import sys
from collections import deque
input = sys.stdin.readline

def delete_first(queue):
    queue.popleft()

def move_left(queue):
    number = queue.popleft()
    queue.append(number)

def move_right(queue):
    number = queue.pop()
    queue.appendleft(number)

n, m = map(int, input().split())
numbers = deque()
wants = deque(list(map(int, input().split())))
count = 0

for i in range(1, n+1):
    numbers.append(i)

while wants:
    if numbers[0] == wants[0]:
        delete_first(numbers)
        delete_first(wants)
    
    else:
        if numbers.index(wants[0]) <= abs(len(numbers) - numbers.index(wants[0]) - 1):
            while numbers[0] != wants[0]:
                move_left(numbers)
                count += 1

        else:
            while numbers[0] != wants[0]:
                move_right(numbers)
                count += 1

print(count)
