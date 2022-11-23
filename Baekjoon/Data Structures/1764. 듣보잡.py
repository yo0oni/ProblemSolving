from sys import stdin

n, m = map(int, input().split())

no_listen = set()
no_see = set()
count = 0

for _ in range(n):
    no_listen.add(stdin.readline().rstrip())
for _ in range(m):
    no_see.add(stdin.readline().rstrip())

result = sorted(list(no_listen & no_see))

print(len(result))
for i in result:
    print(i)