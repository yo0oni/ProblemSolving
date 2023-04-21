def solution(players, callings):
    rank_Dic = {}
    player_Dic = {}

    for i, p in enumerate(players):
        rank_Dic[i + 1] = p
        player_Dic[p] = i + 1
    
    for cur_player in callings:
        cur_rank = player_Dic[cur_player]
        front_rank = cur_rank - 1
        front_player = rank_Dic[front_rank]

        rank_Dic[front_rank], rank_Dic[cur_rank] = rank_Dic[cur_rank], rank_Dic[front_rank]
        player_Dic[front_player], player_Dic[cur_player] = player_Dic[cur_player], player_Dic[front_player]

    return list(rank_Dic.values())