N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))


def solve(r, c, size):
    # 모두 동일하다면
    if check_same(r, c, size):
        return str(arr[r][c])
    else:
        ans = ''
        for i in range(2):
            for j in range(2):
                if i == 0 and j == 0:
                    ans += '('
                next_size = int(size/2)
                ans += solve(r + i * next_size, c + j * next_size, next_size)

                if i == 1 and j == 1:
                    ans += ')'

        return ans


# 모든 원소가 동일한 숫자인지 파악
def check_same(r, c, size):
    val = arr[r][c]

    for i in range(r, r + size):
        for j in range(c, c + size):
            if arr[i][j] != val:
                return False # 하나라도 다를떄

    return True # 모두 동일

print(solve(0, 0, N))