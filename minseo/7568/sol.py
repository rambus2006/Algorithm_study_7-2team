big = []
people = int(input())
# 키랑 몸무게 저장하기
for p in range(people):
    w,h = list(map(int,input().split()))
    big.append([w,h])

cnt=1
# 키 끼리 비교하기
for q in range(people):
    max_w = big[q][0]
    max_h = big[q][1]
    for p in range(people):
        if big[p][0] > max_w and big[p][1] > max_h:
            cnt +=1
    print(cnt,end=" ")
    cnt = 1
