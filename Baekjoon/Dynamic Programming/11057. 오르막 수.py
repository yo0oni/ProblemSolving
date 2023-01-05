n = int(input())
l = [[1] * 10 for i in range(1001)]

# i는 자릿수

# l[1][1] = l[1][0] + l[0][1]
# l[1][2] = l[1][1] + l[0][2]
# l[1][3] = l[1][2] + l[0][3]

# l[2][1] = l[2][0] + l[1][1]
# l[2][2] = l[2][1] + l[1][2]

# l[i][j] = l[i][j-1] + l[i-1][j]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            l[i][j] = 1
        else:
            l[i][j] = l[i][j-1] + l[i-1][j]

print(sum(l[n-1]) % 10007)