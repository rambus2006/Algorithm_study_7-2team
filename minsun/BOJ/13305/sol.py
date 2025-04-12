# 시작 17:16
import sys
sys.stdin = open("input.txt", "r")

N = int(input()) # 도시의 개수를 나타내는 정수
city = list(map(int,input().split()))
cost = list(map(int, input().split()))

min_cost = 999999999
result = 0
for i in range(N-1):
    if cost[i] < min_cost:
        min_cost = cost[i]

    result += (min_cost * city[i])

print(result)


