height = list()

for _ in range(9):
    height.append(int(input()))

sum_ = sum(height)

fake1 = 0
fake2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if sum_ - (height[i]+height[j]) == 100:
            fake1 = height[i]
            fake2 = height[j]

height.remove(fake1)
height.remove(fake2)

height.sort()
for i in height:
    print(i)