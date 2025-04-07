N = int(input())
TP = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    time, pay = TP[i]
    if i + time <= N:
        dp[i] = max(dp[i + 1], dp[i + time] + pay)
    else:
        dp[i] = dp[i + 1]

print(dp[0])
