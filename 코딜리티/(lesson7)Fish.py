def solution(A, B):
    stack = [] # 아래로 내려오는 물고기 저장
    fish_cnt = 0

    for i in range(len(A)):
        token = False

        if B[i] == 1:
            stack.append(A[i])
        elif B[i] == 0:
            # 아래로 내려오는 물고기가 없다면
            if not stack:
                fish_cnt += 1
            else:
                top = stack[-1] # 스택 상단 물고기
                if top > A[i]:
                    continue
                else:
                    while stack:
                        top = stack[-1]
                        # 내려오는 물고기가 더 크다면
                        if top > A[i]:
                            token = True
                            break
                        else:
                            stack.pop()

                    # i번째 물고기 잡아먹힘
                    if token == True:
                        continue
                    else:
                        # i번째 물고기 살아남음
                        fish_cnt += 1

    while stack:
        stack.pop()
        fish_cnt += 1

    return fish_cnt

A = [4,3,2,1,5]
A = [6,3,2,1,5]
B = [1,0,0,0,1]
# B = [0,0,0,0,0]
# B = [1,1,1,1,1]

print(solution(A, B))