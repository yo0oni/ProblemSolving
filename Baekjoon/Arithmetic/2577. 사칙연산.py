a = int(input())
b = int(input())
c = int(input())
cnt = [0]*10

mul = str(a*b*c)

for i in mul:
    cnt[ord(i)-48] += 1

for i in cnt:
    print(i)