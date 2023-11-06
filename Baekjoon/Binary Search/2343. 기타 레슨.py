N, M = map(int, input().split())
videos = list(map(int, input().split()))

result = 0
left, right = max(videos), sum(videos)
while left <= right:
    mid = (left+right)//2

    count, sum_ = 0, 0
    for i in range(N):
        if sum_ + videos[i] > mid:
            count += 1
            sum_ = 0
        sum_ += videos[i]
    if sum_:
        count += 1

    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        result = mid

print(result)