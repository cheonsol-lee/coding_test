def solution(triangle):
    max_list = [triangle[-1]]
    for hier in triangle[-2::-1]:
        hier_max = [max(max_list[-1][i], max_list[-1][i+1]) + hier[i] for i in range(len(hier))]
        max_list.append(hier_max)
    return max_list[-1][0]