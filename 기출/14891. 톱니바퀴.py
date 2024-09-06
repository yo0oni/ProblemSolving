import sys
input = sys.stdin.readline

def left_rotate(list):
  return list[1:] + list[:1] 

def right_rotate(list):
  return list[-1:] + list[:-1]

def rotate(tobni, number, direction):
    if direction == -1:
        tobni[number] = left_rotate(tobni[number])
    else:
        tobni[number] = right_rotate(tobni[number])

def dfs(number, direction, visited):
    visited[number] = True

    if number - 1 >= 0 and not visited[number - 1]:
        if tobni[number][6] != tobni[number - 1][2]:
            dfs(number - 1, (-1) * direction, visited)

    if number + 1 <= 3 and not visited[number + 1]:
        if tobni[number][2] != tobni[number + 1][6]:
            dfs(number + 1, (-1) * direction, visited)

    rotate(tobni, number, direction)

tobni = []
for _ in range(4):
    tobni.append(list(map(int, input().strip())))

k = int(input())
for _ in range(k):
    number, direction = map(int, input().split())
    visited = [False] * 4
    dfs(number - 1, direction, visited)

result = 0
for i in range(4):
    if tobni[i][0] == 1:
        result += (2**i)

print(result)
