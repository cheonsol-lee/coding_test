# 참고: https://leetcode.com/problems/longest-happy-string/discuss/2019507/Simple-python-solution
def solution(A, B, C):
    char_dict = {'A': A, 'B': B, 'C': C}

    ans = ""
    while char_dict['A'] + char_dict['B'] + char_dict['C'] > 0:
        max_char = max(char_dict, key = char_dict.get)

        # 정답 문자열이 최소 2개 문자 이상일 때, 직전의 두 문자가 최대 문자라면
        if len(ans) >= 2 and (ans[-1] == ans[-2] == max_char):
            # 특정 key를 배제하고 다음으로 최대인 문자 선정
            copy_dict = char_dict.copy()
            del copy_dict[max_char]
            max_char = max(copy_dict, key = copy_dict.get)

        # 최대 문자 개수가 0이면 종료
        if char_dict[max_char] == 0:
            return ans
        else:
            ans += max_char
            char_dict[max_char] -= 1

    return ans

A, B, C = 6,1,1
# A, B, C = 1,3,1
# A, B, C = 0,1,8
# A, B, C = 0,0,8
A, B, C = 4,0,0
A, B, C = 4,1,1

print(solution(A, B, C))