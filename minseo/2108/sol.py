'''
n 은 홀수로 나온다.
1. 산술 평균: N개의 수들의 합 / N
2. 중앙값: N개의수를 증가하는 순서로 나열했을 때 중간값
    - 오름차순 sort 없이 하는 법 알아두기
3. 최빈값: 가장 많이 나타나는 값
4. 범위: N개의 수들 중 최대값과 최소값의 차이
이렇게 4가지의 계산을 하는 프로그램
각각의 결과값 출력
n개의 수가 주어짐
N
정수1
정수2
정수3
..
<최빈값 구하는 방법:문제에 '여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.'라는 문구가 있을때>
# 최빈값이 여러개 있는 경우, 두번째로 작은 최빈값을 선택
if len(modearr) > 1 and modearr[0][1] == modearr[1][1]:
#for 문으로 (key,val)형식으로 값을 순회할 때, key에 맞는 val이 가장 앞의 값(최빈값)과 같은 값을 뽑아 그에 맞는 val 값을 반환.
#val == most_common[0][1]:최빈값의 등장 횟수와 같은 숫자들만 뽑기
# 가장 많은 개수인 값 중에서 가장 작은 값을 반환한다.
    mode = sorted([key for key,val in modearr if val == modearr[0][1]])[1]
else:
    mode = modearr[0][0]
'''

'''
def arithmean(n,numbers):
    sumnum = 0
    for num1 in numbers:
        sumnum += num1
    result_arithmean = sumnum//n
    return result_arithmean
'''
'''
def median(n,numbers):
    numbers.sort(reverse=False)
    medianidx = n // 2

    return numbers[medianidx]
'''
'''
def mode(n,numbers):
    arr = []
    for val in numbers:
        cnt=0
        if val in numbers:
            cnt=1
        arr.append(cnt)
    return max(arr)
'''
'''
def scope(n,numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return abs(max_num-min_num)
'''

from collections import Counter
#시작점
n = int(input())
numbers = [int(input()) for _ in range(n)]

#     산술 평균
arithmean = round(sum(numbers)/n)
# 중앙값
numbers.sort(reverse=False)
median = numbers[n // 2]
# 최빈값
# Counter 객체를 만들어 갯수를 세고,가장 많이 등장한 숫자부터 순서대로 리스트를 뽑는 코드 [(1,2),(3,2)...]이런 형식으로 반환된다.
modearr = Counter(numbers).most_common()
candidates = []
max_freq = modearr[0][1]
for key, val in modearr:
    if val == max_freq:
        candidates.append(key)
    else:
        break
candidates.sort()
mode = candidates[1] if len(candidates) > 1 else candidates[0]
#범위
max_num = max(numbers)
min_num = min(numbers)
scope = abs(max_num-min_num)

print(f"{arithmean}\n{median}\n{mode}\n{scope}")