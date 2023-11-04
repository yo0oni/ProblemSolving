import sys
input = sys.stdin.readline

n = int(input())
bulb = list(map(int, input().strip()))
want = list(map(int, input().strip()))

def change(A, B):
    A_copy = A[:]
    count = 0

    for i in range(1, n):
        if A_copy[i-1] == B[i-1]:
            continue
        
        count += 1
        for j in range(i-1, i+2):
            if j < n:
                A_copy[j] = 1 - A_copy[j]

    if A_copy == B:
        return count 
    else:
        return 1e9

result = change(bulb, want)

bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]

result = min(result, change(bulb, want) + 1)

if result != 1e9:
    print(result)
else:
    print(-1)