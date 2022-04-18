p = "(()())()"
# p = ")("
# p = "()))((()"

def check_string(sentence):
    if len(sentence) == 0:
        return ''

    cnt_left = 0
    cnt_right = 0
    stack = []
    answer = ''

    for i in range(len(sentence)):
        # 균형잡힌 괄호 문자열
        if cnt_left == cnt_right and cnt_left != 0:
            u = sentence[:cnt_left+cnt_right]
            v = sentence[cnt_left+cnt_right:]

            # 3. u가 올바른 괄호 문자열이라면 (stack이 비어있음)
            if not stack:
                answer = u + check_string(v)
                return answer
            else:
                answer = '(' + check_string(v) + ')'
                for alpha in u[1:-1]:
                    if alpha == '(':
                        answer += ')'
                    else:
                        answer += '('
                return answer


        if sentence[i] == '(':
            stack.append(sentence[i])
            cnt_left += 1

        if sentence[i] == ')':
            if stack[i-1] == '(':
                stack.pop()

            cnt_right += 1


print(check_string(p))