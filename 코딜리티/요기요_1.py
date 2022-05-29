# 출처: https://molchevskyi.medium.com/best-solutions-for-microsoft-interview-tasks-min-deletions-to-obtain-string-in-right-format-37a3365ce348
def solution(S):
    del_cnt = 0 # 제거할 문자수
    B_cnt = 0

    for s in S:
        if s == 'A':
            # A를 추가로 삭제 or 최소 등장한 B의 개수만큼 삭제
            del_cnt = min(del_cnt+1, B_cnt)
        else:
            B_cnt += 1

    return del_cnt

S = 'BAAABAB'
S = 'BAAABBAB'
# S = 'BBABAA'
# S = 'AABBBB'
# S = 'BAAAABBBB'
S = 'BBAAAABBBB'
print(solution(S))




