import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
numbers = list(map(int, input().split()))

def binary_search(number):
    left = 0
    right = n - 1 # 4

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == number:
            return True

        if number < A[mid]:
            right = mid - 1

        elif number > A[mid]:
            left = mid + 1

for number in numbers:
    if binary_search(number):
        print(1)
    else:
        print(0)