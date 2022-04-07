# 참조(코드): https://donghak-dev.tistory.com/60
# 참조(설명): https://bowbowbow.tistory.com/6
# 참조(유투브): https://youtu.be/yWWbLrV4PZ8


# 실패 테이블 생성 : pattern(찾고자 하는 문자열)
def make_pi(pattern):
    pattern_size = len(pattern)
    pi = [0 for i in range(0, pattern_size)]

    j = 0
    for i in range(1, pattern_size):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        if (pattern[i] == pattern[j]):
            j += 1
            pi[i] = j
    return pi


def KMP(parent, pattern):
    pi = make_pi(pattern)
    parent_size = len(parent)
    pattern_size = len(pattern)
    result = []
    count = 0
    j = 0
    for i in range(0, parent_size):
        while j > 0 and parent[i] != pattern[j]:
            j = pi[j - 1]

        if parent[i] == pattern[j]:
            if j == (pattern_size - 1):
                result.append(i - len(pattern) + 2)
                count += 1
                j = pi[j]
            else:
                j += 1

    print(count)
    for element in result:
        print(element)


T = input()
P = input()
KMP(T, P)