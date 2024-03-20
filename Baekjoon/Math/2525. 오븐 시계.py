import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input())
if b + c < 60:
    print(a, b+c)

else:
    hour = a + (b+c)//60
    minute = (b+c)%60
    if hour >= 24:
        print(hour-24, minute)
    else:
        print(hour, minute)