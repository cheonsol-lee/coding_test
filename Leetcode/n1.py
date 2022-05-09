# 12분 56초
S = 'LILLYBILLYBOO'
L = ['BILL', 'MARIA', 'LILLY']

arr = [0] * 26 # A~Z 배열
for w in S:
    i = ord(w) - ord('A') # index 위치
    arr[i] += 1 # 알파벳에 해당하는 index 증가

max_cnt = 0 # 생성 가능한 단어의 최대수
for word in L:
    min_cnt = 987654321
    for w in word:
        cnt = arr[ord(w) - ord('A')]
        min_cnt = min(min_cnt, cnt)

    max_cnt = max(max_cnt, min_cnt)

print(max_cnt)