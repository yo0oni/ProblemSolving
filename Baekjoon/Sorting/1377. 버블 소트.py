import sys
input = sys.stdin.readline

n = int(input())
changed = False
a = [0]

for _ in range(n):
    a.append(int(input()))


for i in range(1, n+2):
    changed = False

    for j in range(1, n-i+1):
        if a[j] > a[j+1]:
            changed = True
            a[j], a[j+1] = a[j+1], a[j]
    
    if changed == False:
        print(i)
        break