def solution(A):
    num_dict = dict()
    max_sum = 0

    # A리스트 원소의 인덱스를 리스트로 저장
    for i, a in enumerate(A):
        if a not in num_dict:
            num_dict[a] = [i]
        else:
            num_dict[a].append(i)

    for key in num_dict.keys():
        if len(num_dict[key]) >= 2:
            arr = num_dict[key]
            first = arr[0]
            last = arr[-1]
            max_sum = max(max_sum, sum(A[first:last+1]))

    if max_sum != 0:
        return max_sum
    else:
        return -1

A = [1,3,6,1,6,6,9,9]
A = [5,1,4,3]
A = [2,2,2,3,2,3]
print(solution(A))