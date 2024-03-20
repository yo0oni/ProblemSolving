import sys
input = sys.stdin.readline

hour, minute = map(int, input().split())

if minute >= 45:
    print(hour, (minute + 15) % 60)
elif hour-1 < 0:
    print(23, (minute + 15) % 60)
else:
    print(hour-1, (minute + 15) % 60)