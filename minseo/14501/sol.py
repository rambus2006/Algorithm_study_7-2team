'''
T : 상담을 완료하는데 걸리는 기간
P : 상담을 햇을 때 받을 수 있는 금액

기간 : [3,5,1,1,2,4,2]
돈 : [10,20,10,20,15,40,200]
0부터 T까지 순회 t
인덱스 = t(0,1)
while 인덱스 < 기간의 길이
    if 인덱스 >= 기간[t]:
        break
    sum += 돈[인덱스](10,20)
    인덱스 = t(1) + 기간[t](3,5)
    (인덱스 6)
'''
days = []
moneys = []
daylen = int(input())
for d in range(daylen):
    day,money = list(map(int,input().split()))
    days.append(day)
    moneys.append(money)

max_sum = 0
for t in range(daylen):
    index = t
    sum=0
    while index < daylen:
        if index >= daylen:
            if sum >= max_sum:
                max_sum = sum
                break
        sum += moneys[index]
        index = t + days[t]
print(max_sum)
