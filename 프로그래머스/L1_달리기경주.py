def swap_func(cur_player,player_li,players_dict):
    pos = players_dict[cur_player]
    front_player = player_li[pos-1] # 앞선수
    
    players_dict[front_player] += 1
    players_dict[cur_player] -= 1
    
    player_li[pos] = front_player
    player_li[pos-1] = cur_player
    
    return player_li
    
def solution(players, callings):
    player_li = players
    players_dict = dict()
    for i,player in enumerate(player_li):
        players_dict[player] = i
        
    for cur_player in callings:
        player_li = swap_func(cur_player,player_li,players_dict)
        
    return player_li