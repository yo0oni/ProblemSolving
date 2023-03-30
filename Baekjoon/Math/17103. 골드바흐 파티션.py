import sys
input = sys.stdin.readline

# 에라토스테네스의 체 사용하기 !!!
check = [False,False] + [True]*999999

for i in range(2,1000001):
  if check[i]:
    for j in range(2*i, 1000001, i):
        check[j] = False

n = int(input())

for _ in range(n):
    partition = 0
    number = int(input())
    for i in range(2, number//2+1):
       if check[i] and check[number-i]:
          partition += 1
    print(partition)
