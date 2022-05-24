# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    cnt = 0
    stack = [H[0]]  # 높이 저장
    for i in range(1, len(H)):
        if H[i - 1] == H[i]:
            continue
        elif H[i - 1] > H[i]:
            stack.pop()
            cnt += 1

            while stack:
                top = stack[-1]
                if top > H[i]:
                    stack.pop()
                    cnt += 1
                elif top == H[i]:
                    break
                else:
                    stack.append(H[i])
                    break

            if not stack:
                stack.append(H[i])

        else:
            stack.append(H[i])

    while stack:
        stack.pop()
        cnt += 1

    return cnt

H = [8,8,5,7,9,8,7,4,8]
# H = [1,2,3,4,3,2,1]
# H = [4,3,2,1]
# H = [4,4,4]
print(solution(H))