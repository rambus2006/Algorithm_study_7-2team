'''
슬라이싱으로 해결 가능할 것 같다. (조합x)
조합의 합을 구한다. 
최댓값보다 크면 저장 
> 입력값
첫째 줄에는 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어진다. 첫 번째 정수 N은 온도를 측정한 전체 날짜의 수이다. 
N은 2 이상 100,000 이하이다. 두 번째 정수 K는 합을 구하기 위한 연속적인 날짜의 수이다. K는 1과 N 사이의 정수이다. 
둘째 줄에는 매일 측정한 온도를 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -100 이상 100 이하이다.
-> 시간초과가 뜸
> 슬라이딩 윈도우 기법
1. 첫번째 슬라이싱 한 값을 더한다. 
2. 다음 슬라이싱한 값에서 겹치는 값을 뺀다. (새로운 숫자를 더한다. )
'''
import sys

n,k = map(int,sys.stdin.readline().split())
days = list(map(int,sys.stdin.readline().split()))

window_sum = sum(days[:k])
max_day = window_sum
for i in range(k,n):
    window_sum = window_sum - days[i-k] + days[i]
    max_day = max(max_day,window_sum)
print(max_day)