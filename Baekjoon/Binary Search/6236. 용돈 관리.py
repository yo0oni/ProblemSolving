import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]
low = min(array)
high = sum(array)
answer = sum(array)

while low <= high:
    mid = (low+high)//2 # 2001//2 == 1000
    money = 0
    count = 0
    button = False

    for now in array:
        if mid - now < 0:
            button = True
            break
        if money - now < 0:
            money = mid
            count+=1
        money -= now

    if not button:
        if count > m:
            low = mid + 1
        else:
            high = mid - 1
            answer = min(mid, answer)
    
    else:
        low = mid + 1
        
print(answer)