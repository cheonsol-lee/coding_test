# 30분
# A=[2, 3, 1, 4, 2, 2], R=3 일때 [4, 2, 2]를 빼면 남은 값의 종류의 개수가 3으로 최대가 된다.
import copy
A = [2, 3, 1, 4, 2, 2]
R = 3
def solve1(A, R):
    length = len(A)
    A_arr = [0] * 10
    for i in A:
        A_arr[i] += 1

    max_cnt = 0
    i = 0
    while i <= length - R:
        A_copied = copy.deepcopy(A_arr)
        cnt = 0
        for j in A[i:i+R]:
            A_copied[j] -= 1

        for j in range(0, 10):
            if A_copied[j] != 0:
                cnt += 1

        # print(A[i:i+R])
        # print(cnt)

        max_cnt = max(max_cnt, cnt)
        i += 1

    print(max_cnt)

def solve2(A, R):
    max_cnt = 0
    for i in range(len(A) - R):
        cnt = len(set(A[:i] + A[i + R:]))
        max_cnt = max(max_cnt, cnt)

    print(max_cnt)

solve2(A, R)
