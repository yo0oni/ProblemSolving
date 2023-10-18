import math

def getPrimeNumber(n):
    checked = [True]*(n+1)
    prime_numbers = []
    checked[0], checked[1] = False, False

    for i in range(2, int(math.sqrt(n))+1):
        if checked[i]:
            prime_numbers.append(i)
            j = 2

            while i * j <= n:
                checked[i*j] = False
                j += 1

    prime_numbers = [x for x in range(n+1) if checked[x]]
    return prime_numbers

if __name__ == "__main__":
    n = int(input())
    prime_numbers = getPrimeNumber(n)

    right = 1
    left = 0
    count = 0

    while right <= len(prime_numbers):
        prime_sum = sum(prime_numbers[left:right])
        
        if prime_sum == n:
            count += 1
            right += 1

        elif prime_sum < n:
            right += 1

        else:
            left += 1
        
    print(count)