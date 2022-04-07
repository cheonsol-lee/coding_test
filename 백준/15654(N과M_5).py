N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort() #정렬

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    else:
        for i in arr:
            if i not in s:
                s.append(i)
                dfs()
                s.pop()

dfs()