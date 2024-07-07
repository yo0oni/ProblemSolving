import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
b, c = list(map(int, input().split()))
count = 0

for i in range(n):
    people[i] -= b
    count += 1
    
    if people[i] > 0:
        count += (people[i] + c - 1) // c

print(count)