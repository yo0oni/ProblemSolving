import sys
input = sys.stdin.readline

while True:
    abc = list(map(int, input().split()))
    abc.sort()
    c, a, b = abc.pop(), abc.pop(), abc.pop()

    if a == 0 and b == 0 and c == 0:
        break

    if c**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")