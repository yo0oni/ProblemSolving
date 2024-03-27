import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    N = int(input())
    price = list(map(int, input().split()))
    profit, maxPrice = 0, 0

    for i in range(len(price)-1, -1, -1):
        if price[i] > maxPrice:
            maxPrice = price[i]
        else: 
            profit += maxPrice - price[i]

    print(profit)
