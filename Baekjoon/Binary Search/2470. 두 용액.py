import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n - 1
diff = abs(arr[left] + arr[right])
result = [arr[left], arr[right]]

while left < right:
    sum = arr[right] + arr[left]

    if abs(sum) < diff:
        diff = abs(sum)
        result = [arr[left], arr[right]]

        if diff == 0:
            break
    
    if sum < 0:
        left += 1
    else:
        right -= 1

print(*result, sep=' ')