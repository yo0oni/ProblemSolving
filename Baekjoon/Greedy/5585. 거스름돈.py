import sys
input = sys.stdin.readline

price = int(input())
spent = 1000
yen = [500, 100, 50, 10, 5, 1]
change = spent - price

index = 0
count = 0
while change > 0:
    if yen[index] <= change:
        change -= yen[index]
        count += 1
    else:
        index += 1
    
print(count)