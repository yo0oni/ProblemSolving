import sys
from collections import deque
input = sys.stdin.readline

# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
# 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring_summer(trees, food):
    length = len(trees)
    died = deque()
    
    for i in range(length):
        for j in range(length):
            if trees[i][j]:
                trees[i][j].sort()      # 최연소 나무부터 양분 섭취
                alive = deque()
                
                for age in trees[i][j]:
                    if age <= food[i][j]:
                        food[i][j] -= age           # 나이만큼 양분을 섭취
                        alive.append(age + 1)       # 나이 + 1
                    else:
                        died.append((i, j, age))    # 양분 못먹으면 사망
                
                trees[i][j] = alive   
                        
    for x, y, age in died:
        food[x][y] += (age//2)      # 죽은 나무의 나이 // 2 -> 양분


def bfs(trees, ci, cj, n):
    dq = deque(trees[ci][cj])
    
    for age in dq:
        if age % 5 == 0:
            for d in range(8):
                ni, nj = ci + di[d], cj + dj[d]
                
                if 0 <= ni < n and 0 <= nj < n:
                    trees[ni][nj].appendleft(1)     # 나이가 1인 나무 생성
                        
        
def autumn(trees):
    length = len(trees)
    
    for i in range(length):
        for j in range(length):
            if any(num % 5 == 0 for num in trees[i][j]):
                bfs(trees, i, j, length)

def winter(food, robot):
    length = len(food)
    for i in range(length):
        for j in range(length):
            food[i][j] += robot[i][j]

def count_alive(trees):
    length = len(trees)
    count = 0
    
    for i in range(length):
        for j in range(length):
            if trees[i][j]:
                count += len(trees[i][j])
    
    return count

    
def main():
    n, m, k = map(int, input().split())
    trees = [[deque() for _ in range(n)] for _ in range(n)]
    food = [[5 for _ in range(n)] for _ in range(n)]
    robot = [list(map(int, input().split())) for _ in range(n)]
    
    for _ in range(m):
        x, y, z = map(int, input().split())
        trees[x-1][y-1].append(z)
    
    for _ in range(k):
        spring_summer(trees, food)
        autumn(trees)
        winter(food, robot)
    
    print(count_alive(trees))
        

if __name__ == "__main__":
    main()