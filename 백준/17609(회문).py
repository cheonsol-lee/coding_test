T = int(input())

def secondCheck(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            return False
    return True


def firstCheck(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            check1 = secondCheck(word,left+1,right)
            check2 = secondCheck(word,left,right-1)
            if(check1 or check2):
                return 1
            else:
                return 2
    return 0

for _ in range(T):
    word = list(input())
    left=0
    right=len(word)-1
    ans = firstCheck(word,left,right)
    print(ans)