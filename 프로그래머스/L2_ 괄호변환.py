p = "(()())()"
# p = ")("
# p = "()))((()"

def solution(sentence):
    if len(sentence) == 0:
        return ''

    cnt_left = 0
    cnt_right = 0
    stack = []
    answer = ''
    token = True

    for i in range(len(sentence)):
        if cnt_left == cnt_right and cnt_left != 0:
            return check_string(stack, cnt_left, cnt_right, token, sentence)

        if sentence[i] == '(':
            stack.append(sentence[i])
            cnt_left += 1

        if sentence[i] == ')':
            try:
                if stack[-1] == '(':
                    stack.pop()
            except:
                token = False

            cnt_right += 1

    # for문 밖도 동일하게 작동
    return check_string(stack, cnt_left, cnt_right, token, sentence)

def check_string(stack, cnt_left, cnt_right, token, sentence):
    answer = ''

    u = sentence[:cnt_left + cnt_right]
    v = sentence[cnt_left + cnt_right:]

    # 3. u가 올바른 괄호 문자열이라면 (stack이 비어있음)
    if not stack and token == True:
        answer = u + str(solution(v))
        return answer
    else:
        answer = '(' + str(solution(v)) + ')'
        for alpha in u[1:-1]:
            if alpha == '(':
                answer += ')'
            else:
                answer += '('
        return answer

print(solution(p))