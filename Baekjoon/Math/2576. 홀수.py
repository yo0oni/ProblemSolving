l = list()
odd = list()
flag = False
sum = 0
for _ in range(7):
    l.append(int(input()))

for i in l:
    if i%2 !=0:
        flag = True
        odd.append(i)
        sum += i

if flag:
    print(sum)
    print(min(odd))
else:
    print("-1")