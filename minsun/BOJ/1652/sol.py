import sys
sys.stdin = open("input.txt", "r")

def garo():
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    result += 1
                cnt = 0
        if cnt >= 2:
            result += 1

    return result

def sero():
    result = 0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if matrix[i][j] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    result += 1
                cnt = 0
        if cnt >= 2:
            result += 1

    return result

N = int(input())
matrix = [list(map(str, input().strip())) for _ in range(N)]
garo_result = garo()
sero_result = sero()

print(garo_result, sero_result)