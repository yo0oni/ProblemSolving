n = int(input())

for i in range(1,n+1):
    print(" "*(n-i)+"*"*i, end='')
    print("*"*(i-1))
for i in range(1, n):
    print(" "*i+"*"*(n-i), end='')
    print("*"*(n-i-1))
