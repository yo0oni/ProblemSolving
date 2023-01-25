# 1월 1일 -> 101
# 5월 31일 -> 531
# 즉 301보다 크고 1130보다 작아야댐!
# 131 -> 228 -> 331 -> 430 ...

# 301 보다 크고 1130 보다 작아야댐

periods = []
answer = 0
n = int(input())

for _ in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    periods.append((m1*100+d1, m2*100+d2))

periods.sort()

# 정원의 마지막 꽃이 지는 날짜
end_date = 301

# 심은 꽃의 개수
count = 0

while (periods):

    # 정원의 마지막 꽃이 지는 날짜가 12월 1일 이상이 됐거나,
    # 현재 확인할 꽃의 시작 날짜가 정원의 마지막 꽃이 지는 날짜와 이어지지 않을 경우, 탐색 종료
    if (end_date >= 1201 or periods[0][0] > end_date):
        break

    # 꽃이 피는 날짜가 end_date 이전일 때, 가장 느리게 지는 꽃의 날짜
    temp_end_date = -1

    for _ in range(len(periods)):

        # 꽃이 피는 날짜가 end_date 이전이라면,
        if (periods[0][0] <= end_date):
            # 그 중 가장 느리게 지는 꽃의 날짜를 확인
            if (temp_end_date <= periods[0][1]):
                temp_end_date = periods[0][1]

            # 확인한 꽃은 원본 배열에서 제거
            periods.remove(periods[0])

        else:
            break

    # 가장 꽃이 느리게 지는 날짜를 end_date로 수정
    end_date = temp_end_date
    # 심은 꽃의 개수 증가
    count += 1

# 마지막으로 확인한 꽃의 지는 날짜가 12월 1일 보다 작으면, 
# 3월 1일부터 11월 30일까지 계속 피어있는게 아니므로 0 출력
if end_date < 1201:
    print(0)
else:
    print(count)