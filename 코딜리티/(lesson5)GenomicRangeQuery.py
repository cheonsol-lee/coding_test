def solution(S, P, Q):
    ans = []
    for i in range(len(P)):
        A = P[i]
        B = Q[i]
        min_num = 5
        sequence = S[A:B+1]

        if 'A' in sequence:
            num = 1
        elif 'C' in sequence:
            num = 2
        elif 'G' in sequence:
            num = 3
        elif 'T' in sequence:
            num = 4

        # 최솟값 저장
        min_num = min(min_num, num)
        ans.append(min_num)
    return ans

S = 'CAGCCTA'
# S = 'CCCCCCC'
P = [2, 5, 0]
Q = [4, 5, 6]

print(solution(S, P, Q))