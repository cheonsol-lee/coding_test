'''
...!@BaT#*..y.abcdefghijklm
z-+.^.
=.=
123_.def
abcdefghijklmn.p
'''

new_id = input()

# # 1단계
# new_id = new_id.lower()
#
# # 2단계
# answer = ''
# for word in new_id:
#     if word.isalnum() or word in '-_.':
#         answer += word
#
# # 3단계
# while '..' in answer:
#     answer = answer.replace('..', '.')
#
# # 4단계
# answer = answer[1:] if answer[0]=='.' and len(answer)>1 else answer
# answer = answer[:-1] if answer[-1]=='.' else answer
#
# # 5단계
# if not answer: answer = 'a'
#
# # 6단계
# if len(answer) >= 16: answer = answer[:15]
# if answer[-1]=='.': answer = answer[:-1]
#
# # 7단계
# if len(answer) <= 2:
#     last = answer[-1]
#     while len(answer) < 3:
#         answer += last
# print(answer)



# 정규표현식 풀이
import re
st = new_id
st = st.lower() #1단계
st = re.sub('[^a-z0-9-_.]', '', st) #2단계
st = re.sub('\.+', '.', st) #3단계
st = re.sub('^[.]|[.]$', '', st) #4단계
st = 'a' if len(st) == 0 else st[:15] #5단계
st = re.sub('^[.]|[.]$', '', st) #6단계
st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))]) #7단계

print(st)
