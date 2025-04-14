import sys
sys.stdin = open("input.txt", "r")
#############################################

def find(question, num):
    if num == 1:
        return question[0][0]
    temp, div= question.pop()
    while 1:
        for a, b in question:
            if temp % b != a:
                break
        else:
            return temp
        temp += div


T = int(input())
for tc in range(1, T+1):
    num = int(input())
    question = [list(map(int, input().split())) for _ in range(num)]
    question.sort(key=lambda x: x[1])
    result = find(question, num)
    print(f'#{tc} {result}')