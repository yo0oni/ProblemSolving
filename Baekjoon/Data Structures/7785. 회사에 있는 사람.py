import sys
input = sys.stdin.readline

N = int(input())

people = dict()
for _ in range(N):
    name, flag = map(str, input().split())

    if flag == "enter":
        people[name] = True
    else:
        people[name] = False

for name in sorted(people, reverse=True):
    if people[name]:
        print(name)