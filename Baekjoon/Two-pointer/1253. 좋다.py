import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
count = 0

for idx in range(n):
    left = 0
    right = n - 1

    while left < right:
        left_number = numbers[left]
        right_number = numbers[right]

        sum = left_number + right_number
        if sum == numbers[idx]:
            if left == idx:
                left += 1
            elif right == idx:
                right -= 1
            else:
                count += 1
                break

        elif sum < numbers[idx]:
            left += 1

        elif sum >= numbers[idx]:
            right -= 1

print(count)
