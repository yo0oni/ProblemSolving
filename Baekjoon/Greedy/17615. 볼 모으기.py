# 가운데를 기준으로
# (만약 빨간색이 파란색보다 적다면)더 연속된 빨간색이 있는 쪽으로 나머지 빨간색 옮기기?
# 4가지 경우의 수 구한다음 최솟값 출력
# 파란색들을 오른쪽으로, 파란색들을 왼쪽으로, 빨간색들을 오른쪽으로, 빨간색들을 왼쪽으로

n = int(input())
m = list(map(str, input().strip()))
answer = []
blue = red = count = 0

# 우측으로 레드 보내기
for i in range(n):
    if m[i] == "R":
        red += 1

    if m[i] == "B" and red:
        count += red
        red = 0

answer.append(count)

# 우측으로 블루 보내기
count = 0
for i in range(n):
    if m[i] == "B":
        blue += 1

    if m[i] == "R" and blue:
        count += blue
        blue = 0

answer.append(count)

# 좌측으로 레드 보내기
m.reverse()
count = red = 0
for i in range(n):
    if m[i] == "R":
        red += 1
    if m[i] == "B" and red:
        count += red
        red = 0

answer.append(count)

# 좌측으로 블루 보내기
count = blue = 0
for i in range(n):
    if m[i] == "B":
        blue += 1

    if m[i] == "R" and blue:
        count += blue
        blue = 0
        
answer.append(count)

print(min(answer))