def find_leader(A):
    a_dict = {}
    MAX = 1000000001
    criteria = len(A) // 2

    for a in A:
        if a not in a_dict:
            a_dict[a] = 1
        else:
            a_dict[a] += 1

    for a in a_dict.keys():
        if a_dict[a] > criteria:
            return a

    return MAX

def solution(A):
    cnt = 0
    leader = find_leader(A)
    leader_cnt = [0] * len(A)
    total = 0

    # 인덱스별 leader 누적갯수 카운트
    for i in range(len(A)):
        if A[i] == leader:
            total += 1

        leader_cnt[i] = total

    length = len(A)
    MAX_CNT = leader_cnt[-1]

    for i in range(len(A)-1):
        # A[:i+1]구간
        before = leader_cnt[i] > (i+1)//2
        # A[i+1:]구간
        after = (MAX_CNT - leader_cnt[i]) > (length - (i+1))//2

        if before and after:
            cnt += 1

    return cnt


A = [4,3,4,4,4,2]
A = [2,2]
print(solution(A))
