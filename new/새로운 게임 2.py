import sys
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def setting(d):
    if d == 1: # 우
        return 0
    elif d == 2: # 좌
        return 2
    elif d == 3: # 상
        return 3
    else:
        return 1
        

def move():
    global n
    
    for number in range(1, k+1):
        num, si, sj, d = mal[number]
        
        # 1. 해당 위치에 있는 말들 중, 본인 위에 올려진 말들만 가져오기
        start_mal = mal_board[si][sj].index(num)
        mals = mal_board[si][sj][start_mal:]
        
        # 2. 말들 가져온 후 mal_board에 남아있는 애들로만 갱신해주기
        mal_board[si][sj] = mal_board[si][sj][:start_mal]
        
        # 3. 본인의 방향으로 이동할 칸의 색깔 확인하기
        ni, nj = si + di[d], sj + dj[d]
        color = board[ni][nj]
        
        # 4. 색깔 확인한 후 그에 맞는 대응 하기
        if color == 1:
            mals.reverse()
            
        # 4-3. 파란색 : 방향 180도 바꾸기
        elif color == 2:
            d = (d+2) % 4
            ni, nj = si + di[d], sj + dj[d]
            color = board[ni][nj]
            
            # 4-3-1. 바꿨는데 파란색이면 안움직임
            if color == 2:
                ni, nj = si, sj
            elif color == 1:
                mals.reverse()
        
        mal_board[ni][nj].extend(mals)
            
        # 5. 이동한 말들의 위치를 모두 갱신해주기 (본인은 방향도)
        for piece in mals:
            mal[piece][1], mal[piece][2] = ni, nj
        mal[num][3] = d     # 현재 움직인 말의 방향 업데이트
        
        # 6. 4개의 말이 모인 칸이 있는지 확인하기
        for i in range(1, n+1):
            for j in range(1, n+1):
                # 6-1. 있으면 종료
                if len(mal_board[i][j]) >= 4:
                    return True
    return False
        
n, k = map(int, input().split())
board = [[2]* (n+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(n)] + [[2]* (n+2)]
mal_board = [[[] for _ in range(n+2)] for _ in range(n+2)]
mal = [[0, 0, 0]]

for number in range(1, k+1):
    i, j, d = map(int, input().split())
    mal.append([number, i, j, setting(d)])
    mal_board[i][j].append(number)

for i in range(1000):
    if move():
        print(i+1)
        break

else:
    print(-1)