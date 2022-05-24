def solution(S):
    stack = list()
    open_list  = ['(', '[', '{']
    close_list = [')', ']', '}']

    for s in S:
        if s in open_list:
            stack.append(s)
        elif s in close_list:
            # stack이 비어있는데 close값이 들어오면 리턴 0
            if not stack:
                return 0
            else:
                top = stack[-1]
                if top == '(' and s == ')':
                    stack.pop()
                elif top == '[' and s == ']':
                    stack.pop()
                elif top == '{' and s == '}':
                    stack.pop()

    # stack이 비어있음
    if not stack:
        return 1
    # stack이 값이 있음
    else:
        return 0

S = '{[()()]}'
S = '([)()]'
S = '())'
print(solution(S))