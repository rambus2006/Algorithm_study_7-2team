dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def findResult(n, m, arr):
    maxCnt = 0

    for i in range(n):
        for j in range(m):
            cnt = arr[i][j] 
            for d in range(4):
                for k in range(1, arr[i][j] + 1): 
                    nx = i + dx[d] * k
                    ny = j + dy[d] * k
                    if 0 <= nx < n and 0 <= ny < m:
                        cnt += arr[nx][ny]
            maxCnt = max(maxCnt, cnt)
    return maxCnt


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = findResult(n, m, arr)
    print(f"#{tc} {result}")
