# 1초에 1만큼 걷기
# T초에 D만큼 점프하기
import sys
input = sys.stdin.readline

x, y, d, t = map(int, input().split())
dist = (x ** 2 + y ** 2) ** 0.5
if dist >= d:
    # 점프 최대한 + 남은거리 걷기 or 점프 최대한 + 남은거리 걲어서 두번 점프 or 쭉 걷기
    time = min(t * (dist // d) + dist % d, t * ((dist // d) + 1), dist)
else:
    # 점프 한번 + 남은거리 걷기 or 꺾어서 두번 점프 or 쭉 걷기
    time = min(t + (d - dist), 2 * t, dist)

print(time)