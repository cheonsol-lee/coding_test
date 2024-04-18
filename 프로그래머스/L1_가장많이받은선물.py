def solution(friends, gifts):
    friends_num = len(friends)
    
    gift_map = [[0 for i in range(friends_num)] for i in range(friends_num)]
    gift_index_map = [[0,0,0] for i in range(friends_num)]

    name_dict = dict()
    for i,name in enumerate(friends):
        name_dict[name] = i
    
    # 선물 주고받은 행렬
    for gift in gifts:
        gift_li = gift.split()
        i = name_dict[gift_li[0]] # 준 사람
        j = name_dict[gift_li[1]] # 받은 사람
        gift_map[i][j] += 1
    
    # 선물 지수 행렬
    for i in range(friends_num):
        send_gift_cnt = sum(gift_map[i])
        receive_gift_cnt = sum([gift_map[j][i] for j in range(friends_num)])
        gift_index_map[i][0] = send_gift_cnt # 준 선물
        gift_index_map[i][1] = receive_gift_cnt # 받은 선물
        gift_index_map[i][2] = send_gift_cnt-receive_gift_cnt # 선물 지수
    
    # 선물 개수
    gift_num = [0 for i in range(friends_num)]
    
    for i in range(friends_num-1):
        for j in range(i+1, friends_num):
            i_cnt = gift_map[i][j]
            j_cnt = gift_map[j][i]
            
            # i > j
            if i_cnt > j_cnt:
                gift_num[i] += 1
            elif i_cnt < j_cnt:
                gift_num[j] += 1
            elif i_cnt == j_cnt:
                i_index = gift_index_map[i][2]
                j_index = gift_index_map[j][2]
                
                if i_index > j_index:
                    gift_num[i] += 1
                elif i_index < j_index:
                    gift_num[j] += 1
                elif i_index == j_index:
                    continue
            
    answer = max(gift_num)
    return answer
