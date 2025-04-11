import math
inf = -math.inf

n = int(input())
dp = [0] * n
arr = [tuple(map(int, input().split())) for _ in range(n)]

max_val = 0

for i in range(n-1, -1, -1):
    t, p = arr[i]
    if i + t == n:
        max_val = max(max_val, p)
        dp[i] = max_val
        continue
    if i + t > n:
        dp[i] = max_val
        continue
    dp[i] = dp[i+t] + p
    max_val = max(max_val, dp[i])
    dp[i] = max_val

print(max_val)


