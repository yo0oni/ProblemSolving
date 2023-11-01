import sys
input = sys.stdin.readline

m, n = map(int, input().split())
primes = []

def is_prime_number(n):
    if n == 1:
       return False
    
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

for number in range(m, n+1):
  if is_prime_number(number):
     primes.append(number)
     
for prime in primes:
   print(prime)