def solution(A):
    max_switch = 0
    switch = [0] * (len(A) + 1)
    light = [0] * (len(A) + 1)
    light[0] = 1
    cnt = 0
    confirmed = 0 # 확인 완료된 전구

    for a in A:
        switch[a] = 1
        max_switch = max(max_switch, a) # 최대 스위치 번호
        token = False

        # 1번 전구 키기
        if a == 1:
            light[a] = 1
            cnt += 1
            confirmed = 1
            continue

        for i in range(confirmed+1, max_switch+1):
            if switch[i] == 1 and light[i-1] == 1:
                light[i] = 1
            else:
                token = True
                break

        # 전구 모두 on
        if token == False:
            cnt += 1
            confirmed = a

        # print(f'a:{a}, cnt:{cnt}, max_switch:{max_switch}, confirmed:{confirmed}')
    return cnt

A = [2,1,3,5,4]
A = [2,3,4,1,5]
A = [1,3,4,2,5]
A = [5,4,3,2,1]
A = [5,4,3,2,1,6,7]
A = [5,4,3,2,1,7,6]
print(solution(A))