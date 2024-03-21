import sys
input = sys.stdin.readline

h, w = map(int, input().split())
height = list(map(int, input().split()))
tallest_height = height.index(max(height))

right_sum = 0
right_height = height[0]
for i in range(tallest_height):
    if right_height > height[i+1]:
        right_sum += right_height - height[i+1]
    else:
        right_height = height[i+1]

left_sum = 0
left_height = height[-1]
for i in range(w, tallest_height, -1):
    if left_height > height[i-1]:
        left_sum += left_height - height[i-1]
    else:
        left_height = height[i-1]

print(right_sum + left_sum)