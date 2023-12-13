import sys
input = sys.stdin.readline

A, B = map(int, input().split())

count = 1
while True:
    if A > B:
        print(-1)
        break

    if A == B:
        print(count)
        break

    if B % 2 == 0: # 짝수
        B = B // 2


    elif str(B)[-1] == "1":
        B = int(str(B)[:-1])

    else:
        print(-1)
        break
    
    count += 1