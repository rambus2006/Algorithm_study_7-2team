def findResult(n, arr):
    arr.sort()
    minDiff = float('inf')
    possible = False

    for i in range(1, n - 1):  
        for j in range(1, n - i): 
            k = n - i - j 
            if k < 1:
                continue

            smallEnd = i - 1
            midStart = i
            midEnd = i + j - 1
            bigStart = i + j

            smallMax = arr[smallEnd]
            mediumMin = arr[midStart]
            mediumMax = arr[midEnd]
            largeMin = arr[bigStart]

            if smallMax >= mediumMin or mediumMax >= largeMin:
                continue

            smallCnt = i
            mediumCnt = j
            largeCnt = k

            countDiff = max(smallCnt, mediumCnt, largeCnt) - min(smallCnt, mediumCnt, largeCnt)

            if countDiff < minDiff:
                minDiff = countDiff
                possible = True

    if possible:
        return minDiff
    else:
        return -1


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {findResult(n, arr)}')
