import sys
from collections import deque
input = sys.stdin.readline

# 시작 점
# 시작 방향
# 세대

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def curve(x, y, d, g):
    points = [(x, y)]  # 시작 점 추가
    ex, ey = x + dx[d], y + dy[d]
    points.append((ex, ey))
    
    for _ in range(g):
        end_x, end_y = points[-1]  # 끝점
        new_points = []

        for cx, cy in reversed(points):
            nx = end_x + end_y - cy
            ny = end_y - end_x + cx
            new_points.append((nx, ny))

        points.extend(new_points)
    
    return points

def count(points):
    square = 0
    
    for x, y in points:
        if (x+1, y) in points and (x, y+1) in points and (x+1, y+1) in points:
            square += 1
    
    return square

def main():
    n = int(input())
    total_points = set()
    
    for _ in range(n):
        x, y, d, g = map(int, input().split())
        curve_points = curve(x, y, d, g)
        total_points.update(curve_points)
        
    print(count(total_points))
    
if __name__ == "__main__":
    main()