s = input()
cnt=[0]*26

for i in s:
    cnt[ord(i)-97]+=1

for i in cnt:
    print(i, end=' ')