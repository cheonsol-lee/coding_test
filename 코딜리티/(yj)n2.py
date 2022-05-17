# 40분
def solution(A, B):
    if A > B:
       arr = common_process('b', B, 'a', A)
    else:
       arr = common_process('a', A, 'b', B)

    return ''.join(arr)

def common_process(init, init_length, word, word_length):
    arr = [init] * init_length
    word_cnt = 0
    i = 0
    while word_cnt < word_length:
        try:
            if arr[i] == init:
                arr.insert(i, word)
                word_cnt += 1
                i += 2
                # print(arr)
            else:
                i += 1

        # 마지막 부분일 때, 처음으로 돌아옴
        except:
            arr.append(word)
            word_cnt += 1
            i = 0
            # print(arr)

    return arr

# A, B = 5, 3
# A, B = 3, 3
A, B = 1, 4
A, B = 4, 1
# A, B = 1, 0
# A, B = 0, 1

print(solution(A, B))