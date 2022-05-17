#test
def solution(A):
    # 음수 원소 처리
    if max(A) <= 0:
        return 1

    # 단일 원소 처리
    if len(A) == 1 and A[0] > 1:
        return 1

    A = list(set(A))
    A.sort()
    new_A = []

    for i, val in enumerate(A):
        if val > 0:
            new_A.append(val)

    # 양의 정수만 있을때, 제일 작은 값이 1이 아닐 때,
    if min(new_A) != 1:
        return 1

    for i, val in enumerate(new_A):
        try:
            # 현재값에 1을 더한게 다음값이면
            if new_A[i] + 1 == new_A[i+1]:
                continue
            else:
                return new_A[i]+1
        # 마지막까지 순차적으로 들어있다면 마지막 + 1
        except:
            return new_A[i]+1






# A = [1, 3, 6, 4, 1, 2]
# A = [1, 2, 3]
A = [-1, -3]
A = [-1, -3, 0, 1, 2, 4]
A = [2]
A = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17]
A = [3,-1]
print(solution(A))
