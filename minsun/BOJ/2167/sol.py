import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

K = int(sys.stdin.readline())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    result = 0

    for k in range(i-1, x):
        for l in range(j-1, y):
            result+=matrix[k][l]

    print(result)
