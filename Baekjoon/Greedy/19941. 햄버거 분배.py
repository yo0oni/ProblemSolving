import sys
input = sys.stdin.readline

n, k = map(int, input().split())
hams = list(input().strip())

count = 0
for index, ham in enumerate(hams):
    if ham == "P":
        for i in range(index-k, index+k+1):
            if 0 <= i < n and i != index and hams[i] == "H":
                count += 1
                hams[i] = "F"
                break

print(count)