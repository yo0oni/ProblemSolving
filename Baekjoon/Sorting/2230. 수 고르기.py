import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for idx in range(n):
    arr.append(int(input()))

arr.sort()
answer = sys.maxsize
left = right = 0

while left <= right and right < n:
    diff = arr[right] - arr[left]
    
    if diff < m:
        right += 1
    
    else:
        left += 1
        answer = min(diff, answer)
    
print(answer)