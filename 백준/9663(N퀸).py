N = int(input())

cnt = 0
row = [0] * N # 행마다 저장되는 퀸의 열 위치

def is_promising(x):
    # x행보다 적은 행(위쪽 체스판)의 조건 비교
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    return True

def n_queen(x):
    global cnt
    if x == N:
        cnt += 1
        return
    else:
        # x행에 대한 i열 위치에 퀸 저장
        for i in range(N):
            row[x] = i

            if is_promising(x):
                n_queen(x + 1)

n_queen(0)

print(cnt)