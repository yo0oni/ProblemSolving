import sys
input = sys.stdin.readline

n = int(input())
br = list(input().strip())

blue, red = 0, 0
temp = ""
for color in br:
    if color == "B" and temp != "B":
        blue += 1
        temp = "B"
    elif color == "B" and temp == "B":
        continue
    elif color == "R" and temp != "R":
        red += 1
        temp = "R"
    elif color == "R" and temp == "R":
        continue
        

if red < blue:
    count = 0
    flag = False
    for i in range(n):
        if br[i] == "R" and flag:
            continue
        elif br[i] == "R" and not flag:
            count += 1
            flag = True
        else:
            flag = False

    print(count+1)

else:
    count = 0
    flag = False
    for i in range(n):
        if br[i] == "B" and flag:
            continue
        elif br[i] == "B" and not flag:
            count += 1
            flag = True
        else:
            flag = False
            
    print(count+1)