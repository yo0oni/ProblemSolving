import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
v = int(input())

count = 0
for number in numbers:
    if number == v:
        count += 1
    
print(count)