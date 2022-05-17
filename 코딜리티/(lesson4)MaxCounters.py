def solution(N, A):
    counters = [0] * N
    max_val = 0
    save_max_val = 0

    for val in A:
        if val <= N:
            if counters[val-1] < save_max_val:
                counters[val-1] = save_max_val
            counters[val-1] += 1
            max_val = max(max_val, counters[val-1])
        elif val == N + 1:
            save_max_val = max_val # 최댓값을 임시 저장 (모든 값을 호출할 때마다 갱신할 예정)

    for i in range(N):
        if counters[i] < save_max_val:
            counters[i] = save_max_val

    return counters

A = [3,4,4,6,1,4,4]
# A = [3]
# A = [1,1,1,1,1,1,1,1]
# A = [1,6]
# A = [6,2]
# A = [1,6,2]
N = 5
counters = solution(N, A)
print(counters)