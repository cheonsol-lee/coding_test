'''
1. 인접한 두 칸을 골라 사탕을 교환 후 전체 보드를 탐색하여 같은 색의 연속된 개수 파악
2. 사탕의 최대 개수(max_count)보다 구한 사탕 개수(count)가 더 크면 count로 대체
3. 교환한 사탕을 원래대로 복귀
4. 1~3 과정 반복
5. max_count 출력
'''

N = int(input())
data = [list(input()) for i in range(N)]

max_count = 0

def width():
    global max_count
    
    for i in range(N):
        count = 1
        for j in range(1, N):
            if data[i][j] == data[i][j-1]:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 1
        if max_count < count: # 한줄이 모두 같은 경우
            max_count = count
            
def height():
    global max_count
    
    for i in range(N):
        count = 1
        for j in range(1, N):
            if data[j][i] == data[j-1][i]:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 1
        if max_count < count: # 한줄이 모두 같은 경우
            max_count = count
            
for i in range(N):
    for j in range(1, N):
        # 열끼리 비교
        data[i][j], data[i][j-1] = data[i][j-1] , data[i][j] # 교환
        width()
        height()
        data[i][j], data[i][j-1] = data[i][j-1] , data[i][j] # 복귀
        
        # 행끼리 비교
        data[j][i], data[j-1][i] = data[j-1][i] , data[j][i] # 교환
        width()
        height()
        data[j][i], data[j-1][i] = data[j-1][i] , data[j][i] # 복귀
        
print(max_count)