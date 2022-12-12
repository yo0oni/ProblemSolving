n = int(input())

for i in range(1, n+1):
    print("*"*i+" "*(n-i), end='')
    print(" "*(n-i)+"*"*i)
for i in range(1, n):
    print("*"*(n-i)+" "*i, end='')
    print(" "*i+"*"*(n-i))