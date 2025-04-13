import sys
sys.stdin = open("input.txt", "r")

"""
0 : 빈칸, 1: 벽, 2 : 괴물
"""
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                for dx, dy in dxy:
                    for k in range(N):
                        nx = i + dx * k
                        ny = j + dy * k

                        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 1:
                            matrix[nx][ny] = 3
                        else:
                            break


    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                cnt += 1

    print(f"#{tc}", cnt)



