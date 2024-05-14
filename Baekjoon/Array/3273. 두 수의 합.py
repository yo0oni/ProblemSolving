import sys
input = sys.stdin.readline

n = int(input())
numbers = sorted(list(map(int, input().split())))
want = int(input())

count = 0
left, right = 0, n - 1

while left < right:
    temp = numbers[left] + numbers[right]

    if temp == want:
        count += 1
        left += 1

    elif temp < want:
        left += 1

    else:
        right -= 1

print(count)