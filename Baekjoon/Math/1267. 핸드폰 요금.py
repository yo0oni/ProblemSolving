n = int(input())
t = list(map(int,input().split()))
m = y = 0

for i in t:
    y += (i//30+1)*10
    m += (i//60+1)*15
    
if m==y:
    print("Y M", m)
elif m>y:
    print("Y", y)
else:
    print("M", m)
