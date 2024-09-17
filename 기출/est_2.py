from collections import Counter
from collections import deque

def solve(queue):
    N = len(queue)/3 # 최종 원소 개수
    result = [0,0,0] # 추가한 원소 개수
    
    dq = deque([])
    for i in queue:
        dq.append(i)
    counter = Counter(dq)

    while True:
        cnt = 0 # 동일한 원소개수
        counter = Counter(dq)
        for key in [1,2,3]:
            if counter[key] == N:
                cnt += 1
                continue
            elif counter[key] < N:
                dq.append(key)
                dq.popleft()
                result[key-1] += 1
        if cnt == 3:
            break
    return result


queue = [2,1,3,1,2,1]
queue = [3,3,3,3,3,3]
queue = [1,2,3]
queue = [1,3,1,2,2,2]
queue = [3,2,3]
print(solve(queue))