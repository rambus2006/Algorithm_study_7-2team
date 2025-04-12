import sys
sys.setrecursionlimit(10 ** 5)
m, n = map(int, sys.stdin.readline().rstrip().split())

dxl = [0, 1, 0, -1]
dyl = [1, 0, -1 , 0]
def dfs(x, y, num):
    if dp[x][y] > -1:
        return dp[x][y]
    cnt = 0
    for dx, dy in zip(dxl, dyl):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < m and 0 <= ny < n and num > arr[nx][ny]:
            cnt += dfs(nx, ny, arr[nx][ny])
    dp[x][y] = cnt
    return dp[x][y]

dp = [[-1] * n for _ in range(m)]
dp[m-1][n-1] = 1
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

dfs(0,0,arr[0][0])
print(dp[0][0])
