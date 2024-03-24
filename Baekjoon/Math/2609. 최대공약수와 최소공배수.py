import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())
print(math.gcd(a, b)) # 최대공약수
print(math.gcd(a, b) * (a // math.gcd(a, b)) * (b // math.gcd(a, b)))