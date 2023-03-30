import sys
input = sys.stdin.readline

a, b = map(int, input().split())
setA = set()
setB = list()
for _ in range(a):
    setA.add(input().replace("\n",""))
for _ in range(b):
    setB.append(input().replace("\n",""))

result = 0
for _ in range(b):
    str = setB.pop()
    if str in setA:
        # print(str)
        result += 1

print(result)
