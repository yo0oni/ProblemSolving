import sys
from itertools import combinations
input = sys.stdin.readline


n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
    
# 적 위치 저장
def find_target_location():
    targets = set()
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                targets.add((i, j))
    
    return targets
    
    
# 궁수들과의 거리 비교해서 가장 가까운 적들 저장 -> 중복 공격 ㄱㄴ
def find_target(archer_x, archer_y, targets):
    min_distance = float('inf')
    target = None
    
    for target_x, target_y in targets:
        distance = abs(target_x - archer_x) + abs(target_y - archer_y)
        
        # 조건: 거리 우선, 왼쪽 우선
        if distance <= d:
            if distance < min_distance:
                min_distance = distance
                target = (target_x, target_y)
            elif distance == min_distance and target_y < target[1]:
                target = (target_x, target_y)

    return target
           
           
def move_down(targets):
    new_targets = set()
    
    for x, y in targets:
        if x + 1 < n:
            new_targets.add((x + 1, y))
            
    return new_targets
        

def simulate(archers):
    targets = find_target_location()
    count = 0
    
    while targets:
        attack_targets = set()
        
        # 공격할 적 선정
        for archer_y in archers:
            target = find_target(n, archer_y, targets)
            if target:
                attack_targets.add(target)
        
        # 적 공격
        for target in attack_targets:
            if target in targets:
                count += 1
                targets.remove(target)
        
         
        # 적들 한칸 아래로   
        targets = move_down(targets)
    
    return count


max_kills = 0
for archer_positions in combinations(range(m), 3):
    kills = simulate(archer_positions)
    max_kills = max(max_kills, kills)

print(max_kills)