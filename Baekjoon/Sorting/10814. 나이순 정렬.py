import sys
input = sys.stdin.readline

N = int(input())
users = []

number = 0
for _ in range(N):
    age, name = map(str, input().split())
    users.append((int(age), number, name))
    number += 1

users.sort(key=lambda x: (x[0], x[1]))
for index in range(N):
    print(users[index][0], users[index][2])