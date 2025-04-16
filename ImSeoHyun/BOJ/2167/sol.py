n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

psum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    rowSum = 0
    for j in range(1, m + 1):
        rowSum += arr[i - 1][j - 1]
        psum[i][j] = psum[i - 1][j] + rowSum

for _ in range(k):
    i, j, x, y = map(int, input().split())

    result = psum[x][y]- psum[i - 1][y]- psum[x][j - 1]+ psum[i - 1][j - 1]
    
    print(result)
