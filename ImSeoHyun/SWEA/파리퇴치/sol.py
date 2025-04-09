T = int(input())

def findResult(n, m, arr): 
    maxCnt = 0
    for i in range(n - m + 1): 
        for j in range(n - m + 1): 
            cnt = 0
            for x in range(i, i + m): 
                for y in range(j, j + m): 
                    cnt += arr[x][y]
            maxCnt = max(maxCnt, cnt)
    return maxCnt

for tc in range(1, T + 1): 
    n , m = map(int , input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = findResult(n, m, arr)
    print(f"#{tc} {result}")
