import sys
input = sys.stdin.readline

a = list(input().strip())
b = list(input().strip())

index = 0
while index < len(a):
    if a[index] in b:
        b.remove(a[index])
        a.remove(a[index])
        index -= 1
    index += 1

print(len(a) + len(b))