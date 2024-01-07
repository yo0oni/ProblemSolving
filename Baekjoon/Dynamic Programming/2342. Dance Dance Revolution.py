import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def move(a, b):
    if a == b: # 같은 발판
        return 1
    elif a == 0: # 0에서 이동
        return 2
    elif abs(b - a) % 2 == 0: # 반대편 발판
        return 4
    else: # 인접 발판
        return 3


# 발의 위치가 left, right 일 때, number번째 발판을 밟았을 때 소모되는 힘
def solve(number, left, right):
    global dp

    if number == len(arr) - 1:
        return 0

    if dp[number][left][right] != -1:
        return dp[number][left][right]

    dp[number][left][right] = min(solve(number + 1, arr[number], right) + move(left, arr[number]),
                                  solve(number + 1, left, arr[number]) + move(right, arr[number]))
    
    return dp[number][left][right]

arr = list(map(int, input().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(100000)]
print(solve(0, 0, 0))