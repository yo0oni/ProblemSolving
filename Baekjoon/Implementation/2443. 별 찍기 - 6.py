n = int(input())

for i in range(n):
    print(" "*i+"*"*(n-i), end='')
    print("*"*(n-i-1))