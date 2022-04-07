# 참고 : https://youtu.be/z4wKvYdd6wM
N = int(input())
col = [0] * (N+1) # 특정 행에 놓인 퀸의 컬럼 번호
cnt = 0
def n_queens(col, i):
    global cnt
    n = len(col) - 1

    if promising(col, i):
        if i == n:
            cnt += 1
            # print(col[1: n+1])
        else:
            for j in range(1, n+1):
                col[i + 1] = j
                n_queens(col, i + 1)

def promising(col, i):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == abs(i-k):
            flag = False
        k += 1

    return flag



n_queens(col, 0)
print(cnt)