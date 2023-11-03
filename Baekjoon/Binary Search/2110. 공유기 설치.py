import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = []

for _ in range(n):
    home.append(int(input()))
home.sort()

start = 1
end = home[-1] - home[0]
result = 0

if c == 2:
    print(home[-1] - home[0])

else:
    while start < end:
        mid = (start + end) // 2
        count = 1
        wifi = home[0]

        for i in range(n):
            if home[i] - wifi >= mid:
                count += 1
                wifi = home[i]

        if count >= c:
            result = mid
            start = mid + 1

        elif c > count:
            end = mid

    print(result)