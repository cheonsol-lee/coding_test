id_dict = {}
act_list = [] # 활동 순서 기록
record = ["Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan"]
answer = []

for s in record:
    s = s.split()

    # 상태, ID
    act_list.append([s[0], s[1]])

    if s[0] == 'Enter' or s[0] == 'Change':
        id_dict[s[1]] = s[2] # ID : 이름

# print(act_list)

for s in act_list:
    nickname = id_dict[s[1]]
    if s[0] == 'Change':
        continue
    if s[0] == 'Enter':
        answer.append(f'{nickname}님이 들어왔습니다.')
        # print(f'{nickname}님이 들어왔습니다.')
    if s[0] == 'Leave':
        answer.append(f'{nickname}님이 나갔습니다.')
        # print(f'{nickname}님이 나갔습니다.')

print(answer)