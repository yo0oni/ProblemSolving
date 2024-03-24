import sys, math
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

def primenumber(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
            return False
    return True

count = 0
for number in numbers:
    if primenumber(number):
        count += 1

print(count)