import sys
input = sys.stdin.readline

n = int(input())
sixs = []
i = 0
while n:
    if "666" in str(i):
        sixs.append(i)
        n -= 1
    i += 1
    
print(sixs[-1])