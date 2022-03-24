S = int(input())

total = 0
i = 1
count = 0

while True:
    total += i
    i += 1
    count += 1 # 숫자 갯수

    # 입력 수를 찾았다면
    if total == S:
        print(count)
        break

    elif total > S:
        print(count-1)
        break



