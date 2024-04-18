def solution(v):
    # x, y좌표가 들어갈 리스트
    x = []
    y = []
    answer = []

    # 이중배열 순회
    for i in v:
        if i[0] not in x:
            x.append(i[0])
        else:
            x.remove(i[0])
        if i[1] not in y:
            y.append(i[1])
        else:
            y.remove(i[1])

    answer = x + y

    return answer


v = [[1, 4], [3, 4], [3, 10]]
# v = [[1, 1], [2, 2], [1, 2]]
print(solution(v))