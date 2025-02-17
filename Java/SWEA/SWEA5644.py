import collections

di = [0, 0, 1, 0, -1]
dj = [0, -1, 0, 1, 0]

def validate(i, j):
    return 0 <= i < 11 and 0 <= j < 11

test_case = int(input())
for tc in range(1, test_case+1):
    
    # M : 총 이동시간
    # A : BC 개수
    M, A = map(int, input().split())
    alst = list(map(int, input().split()))
    blst = list(map(int, input().split()))
    b_total, a_total = 0, 0
    a_si, a_sj = 1, 1
    b_si, b_sj = 10, 10
    
    board = [[[] for _ in range(11)] for _ in range(11)]
    bc_ability = collections.defaultdict(int)
    
    for num in range(1, A+1):
        si, sj, c, p = map(int, input().split())
        board[sj][si].append(num)
        bc_ability[num] = p
        
        for ni in range(1, 11):
            for nj in range(1, 11):
                if abs(ni-si) + abs(nj-sj) <= c and validate(ni, nj):
                    board[nj][ni].append(num)
    
    if len(board[a_sj][a_si]):
        max_ability = 0
            
        for num in board[a_sj][a_si]:
            ability = bc_ability[num]
            
            if ability > max_ability:
                max_ability = ability
                
        a_total += max_ability

    if len(board[b_sj][b_si]):
        max_ability = 0
            
        for num in board[b_sj][b_si]:
            ability = bc_ability[num]
            
            if ability > max_ability:
                max_ability = ability
                
        b_total += max_ability
    
    # A랑 B 동시 이동
    for time in range(M):
        a_dir = alst[time]
        b_dir = blst[time]
        
        a_ni = a_si + di[a_dir]
        a_nj = a_sj + dj[a_dir]
        
        b_ni = b_si + di[b_dir]
        b_nj = b_sj + dj[b_dir]
        
        # 둘다 충전소
        if len(board[a_nj][a_ni]) and len(board[b_nj][b_ni]):
            max_ability = 0
            max_a, max_b = 0, 0
                        
            for a in board[a_nj][a_ni]:
                for b in board[b_nj][b_ni]:
                    if a == b:
                        ability = [bc_ability[a]//2, bc_ability[a]//2]
                        sum_ability = sum(ability)
                        
                        if sum_ability > max_ability:
                            max_ability = sum_ability
                            max_a = bc_ability[a]//2
                            max_b = bc_ability[a]//2
                    
                    else:
                        ability = [bc_ability[a], bc_ability[b]]
                        sum_ability = sum(ability)
                        
                        if sum_ability > max_ability:
                            max_ability = sum_ability
                            max_a = bc_ability[a]
                            max_b = bc_ability[b]
            
            a_total += max_a
            b_total += max_b

            
        elif board[b_nj][b_ni] and not board[a_nj][a_ni]:
            max_ability = 0
            
            for num in board[b_nj][b_ni]:
                ability = bc_ability[num]
                
                if ability > max_ability:
                    max_ability = ability
                    
            b_total += max_ability
        
        elif board[a_nj][a_ni] and not board[b_nj][b_ni]:
            max_ability = 0
            
            for num in board[a_nj][a_ni]:
                ability = bc_ability[num]
                
                if ability > max_ability:
                    max_ability = ability
                    
            a_total += max_ability
        
        a_si, a_sj = a_ni, a_nj
        b_si, b_sj = b_ni, b_nj
        
    print(f"#{tc} {a_total + b_total}")