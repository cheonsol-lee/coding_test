def solution(S, C):
    s_dict = dict()
    MAX = 987654321
    cost = 0
    for i, s in enumerate(S):
        if s not in s_dict:
            s_dict[s] = [i]
        else:
            s_dict[s].append(i)

    for key in s_dict.keys():
        arr = s_dict[key]

        while len(arr) >= 2:
            min_cost = MAX
            min_index = -1

            for i in range(1, len(arr)):
                if arr[i - 1] + 1 == arr[i]:
                    if min_cost > C[arr[i-1]]:
                        min_cost = C[arr[i-1]]
                        min_index = i-1

                    if min_cost > C[arr[i]]:
                        min_cost = C[arr[i]]
                        min_index = i

            if min_cost != MAX:
                cost += min_cost
                arr.pop(min_index)

            else:
                break

    return cost


S = 'abccbd'
C = [0,1,2,3,4,5]

S = 'aabbcc'
C = [1,2,1,2,1,2]

S = 'aaaa'
C = [3,4,5,6]

S = 'ababa'
C = [10,5,10,5,10]

S = 'acaab'
C = [3,4,5,6,7]

S = 'abcd'
C = [3,4,5,6]

S = 'abbb'
C = [3,4,5,6]
print(solution(S, C))