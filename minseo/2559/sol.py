'''
N : 온도를 측정한 전체 날짜의 수
K : 합을 구하기 위한 연속적인 날짜의 수

10 2
3 - 2 = 1
-2 - 4 = -6
-4 - 9  = -13
-9 + 0 = -9
0 + 3 = 3
3 + 7 = 10
7 + 13 = 20
13 + 8 = 21
8 - 3 = 5

1)
n개를 순회할 때
모두 탐색하는 것이 아닌 값에 음수가 섞여있으면 건너 뛰어야 한다.
K개씩 묶은 뒤 음수가 안섞여있으면 합친다.
이때 음수가 섞여있으면 continue 한다.
합을 구한다.
만약 합을 구한 값이 max 값보다 큰 경우
max값을 바꾼다.
마지막에 max 값만 출력하낟.
    # 음수인 경우 미리 거르기
    # for inside in range(K):
    #     if days[l][inside] < 0:
    #         continue
    #     else:
    #         sumtmp += days[l][inside]
    #         if sumtmp > max_tmp:
    #             max_tmp = sumtmp
    #             sumtmp = 0
    # sumdays = sum(days[l])
2)
음수를 전부 0으로 변경
만약 0이 포함되면 거르기
0이 아닌 경우에만 더하기
3)
누적합
- 누적합 배열 만들기
- 누적합 배열[끝점] - 누적합 배열[시작점-1]을 하면 구간의 값이 나온다.
'''
N , K = list(map(int,input().split()))
daytmp = list(map(int,input().split()))
sumtmp = 0
max_tmp = 0

current = sum(daytmp[:K])
max_tmp = current

for i in range(1,N - K + 1):
    current = current - daytmp[i - 1] + daytmp[i + K - 1]
    if current > max_tmp:
        max_tmp = current
print(max_tmp)