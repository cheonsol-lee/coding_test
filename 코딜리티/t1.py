def solution(logs):
    answer = []
    problem_dict = dict()
    problem_list = []
    user_list = []
    new_logs = []

    # 중복제거
    for log in logs:
        problem_list.append(log.split())
    logs = set(map(tuple, problem_list))
    for log in logs:
        if log not in new_logs:
            new_logs.append(log)

    # dictionary 생성
    for log in new_logs:
        user = log[0]
        title = log[1]

        if title not in problem_dict:
            problem_dict[title] = 1
        else:
            problem_dict[title] += 1

        if user not in user_list:
            user_list.append(user)

    # 웰노운 찾기
    user_cnt = len(user_list) # 유저수
    boundary = int(user_cnt // 2) if user_cnt % 2 == 0 else int(user_cnt // 2 + 1)# 경계(절반 이상)

    for problem in problem_dict.keys():
        if problem_dict[problem] >= boundary:
            answer.append(problem)

    # 정렬
    answer.sort()

    return answer



logs = ["morgan string_compare", "felix string_compare", "morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]
# logs = ["morgan string_compare","morgan string_compare", "felix string_compare", "morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]
# logs = ["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"]
# logs = ["kate sqrt"]
print(solution(logs))