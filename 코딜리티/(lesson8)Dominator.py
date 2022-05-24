def solution(A):
    criteria = len(A) // 2
    MAX = 2147483648
    dominator = MAX
    a_dict = {}

    for i in range(len(A)):
        if A[i] not in a_dict:
            a_dict[A[i]] = 1
        else:
            a_dict[A[i]] += 1

    # 원소 갯수가 절반 이상일 때
    for key in a_dict.keys():
        if a_dict[key] > criteria:
            dominator = key
            break

    if dominator != MAX:
        return A.index(dominator)
    else:
        return -1

A = [3,4,3,2,3,-1,3,3]
A = [1,2,3,4,5,5,5,5,5]
print(solution(A))