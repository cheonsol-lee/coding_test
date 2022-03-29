num_16 = list(input())
num_16.reverse() # 문자열 뒤집기
total = 0
for i in range(len(num_16)):
    try:
        # 0 ~ 9 까지
        num = int(num_16[i])
        total += num * (16 ** i)
    except:
        # A ~ E 까지
        num = num_16[i]
        total += (ord(num) - ord('A') + 10) * (16 ** i)

print(total)