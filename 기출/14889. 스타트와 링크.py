import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
min_diff = 1e9

def get_diff(start, link):
    start_ability, link_ability = 0, 0
    for i in range(n//2):
        for j in range(n//2):
            start_ability += board[start[i]][start[j]]
            link_ability += board[link[i]][link[j]]
            
    return abs(start_ability - link_ability)

def dfs(player, start, link):
    global min_diff
    if player == n:
        if len(start) == len(link):
            min_diff = min(min_diff, get_diff(start, link))
        return
    
    dfs(player+1, start+[player], link)
    dfs(player+1, start, link+[player])

dfs(0, [], [])
print(min_diff)