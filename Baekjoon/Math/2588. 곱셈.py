import sys
input = sys.stdin.readline

a = int(input())
b = list(input().strip())

number_list = []
base = 1

while b:
    number = int(b.pop()) * a
    number_list.append(number * base)
    base *= 10
    
    print(number)

print(sum(number_list))