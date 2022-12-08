l = list(map(int, input().split()))

a = min(l)
b = max(l)

n = b-a-1

if a == b or a+1 == b:
    n = 0
print(n)

for i in range(a+1, b):
    print(i, end=' ')