import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def gcd(a, b):
    a = int(a)
    b = int(b)
    while b > 0:
        a, b = b, a % b
    return a

print('1'*gcd(A, B))