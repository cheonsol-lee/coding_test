s = input()
length = len(s)

# 참고: https://pearlluck.tistory.com/589
# 과정
# 1. N개 단위로 문자열 자름
# 2. 자른 문자열을 가지고 압축 문자열 만듦
# 3. 슬라이싱한 문자열의 개수가 1일 때, cnt 생략
# 4. 길이가 가장 짧은 것 리턴
def solution(s):
    ans = 10000

    # 반복되는 문자열 길이 n
    for n in range(1, len(s)//2 + 2):
        res = ''
        cmp_str = s[:n] # 비교문자열
        cnt = 1

        for i in range(n, len(s) + n, n):
            cur_str = s[i : i+n]
            if cmp_str == cur_str:
                cnt += 1
            else:
                if cnt == 1:
                    res += cmp_str
                else:
                    res += str(cnt) + cmp_str

                cmp_str = cur_str
                cnt = 1

        ans = min(ans, len(res))

    return ans

print(solution(s))
