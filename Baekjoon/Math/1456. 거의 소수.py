import math, sys
input = sys.stdin.readline

min, max = map(int, input().split())
a=[0]*(10000001)# 10^7

for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(math.sqrt(len(a))+1)):
   if a[i] == 0:
       continue
   
   for j in range(i+i, len(a), i):
       a[j] = 0

count=0
for i in range(2, 10000001):
    if a[i]!= 0:
        tmp = a[i]

        while a[i] <= max/tmp:
            if a[i] >= min/tmp:
                count += 1

            tmp = tmp * a[i]

print(count)