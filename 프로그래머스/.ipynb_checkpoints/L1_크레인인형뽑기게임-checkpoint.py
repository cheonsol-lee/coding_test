# 소요시간: 35분 39초

def select_dolls(board, move):
    N = len(board) # 맵의 세로 크기
    
    for i in range(N):
        doll = board[i][move-1] # 현재 위치의 인형
        if doll != 0 :
            # 인형이 있다면
            board[i][move-1] = 0 # 빈칸으로 변경
            break
        else:
            # 인형이 없다면
            continue
            
    return board, doll
    
def check_basket(basket, doll):
    if doll == 0:
        # 인형을 뽑지 못했다면
        return basket, 0
        
    else:
        basket_size = len(basket)
        if basket_size == 0:
            # 빈 바구니
            basket.append(doll)
            return basket, 0
        else:
            if basket[-1] != doll:
                # 맨 위 인형이 다르다면
                basket.append(doll)
                return basket, 0
            else:
                # 맨 위 인형이 같다면
                basket.pop() # 하나꺼내고, 2개를 터뜨림
                return basket, 2

def solution(board, moves):
    basket = [] # 뽑은 인형 바구니
    answer = 0 # 사라진 인형수
    
    for move in moves:
        board, doll = select_dolls(board, move)
        basket, cnt_doll = check_basket(basket, doll) # 출력: 바구니, 사라진 인형
        answer += cnt_doll
        
    return answer