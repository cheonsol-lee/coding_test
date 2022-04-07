N, M = map(int, input().split())
s = [] # 숫자 저장 리스트

def dfs():
    # 문자열의 길이가 M이 되면 출력
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    else:
        for i in range(1, N+1):
            if i not in s:
                s.append(i)
                dfs()
                s.pop()

dfs()