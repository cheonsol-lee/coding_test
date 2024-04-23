def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
