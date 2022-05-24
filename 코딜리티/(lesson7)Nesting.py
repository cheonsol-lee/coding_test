def solution(S):
    stack = []

    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return 0

            if stack[-1] == '(':
                stack.pop()

    # stack이 비어있다면 정상 종료
    if not stack:
        return 1
    else:
        return 0

S = '(()(())())'
S = '())'
print(solution(S))