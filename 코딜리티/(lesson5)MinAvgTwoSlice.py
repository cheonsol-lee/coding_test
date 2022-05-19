def solution(A):
    N = len(A)
    min_val = sum(A[0:2])/2
    ans = 0
    # 원소가 2개만 있으면 0번째 인덱스 출력
    if N == 2: return ans

    for i in range(3, N+1):
        # 슬라이스 3칸
        avg = sum(A[i - 3:i]) / 3
        if avg < min_val:
            min_val = avg
            ans = i - 3

        # 슬라이스 2칸
        avg = sum(A[i-2:i]) / 2
        if avg < min_val:
            min_val = avg
            ans = i-2

    return ans

# A = [4, 2, 2, 5, 1, 5, 8]
# A = [9,9,9]
A = [2,3,1]
print(solution(A))