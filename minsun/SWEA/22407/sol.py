import sys
sys.stdin = open("input.txt", "r")

def drawing(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            white_board[i][j] += 1


T = int(input())
for tc in range(1, T+1):
    N = 10
    white_board = [[0]*N for _ in range(N)]
    row = col = 0
    r_r1, r_c1, r_r2, r_c2 = map(int, input().split()) # 빨간색
    b_r1, b_c1, b_r2, b_c2 = map(int, input().split()) # 파란색

    drawing(r_r1, r_c1, r_r2, r_c2)
    drawing(b_r1, b_c1, b_r2, b_c2)

    for k in range(N):
        row = 0
        for l in range(N):
            if white_board[k][l] == 2:
                row += 1
        if row > 0:
            break

    for m in range(N):
        col = 0
        for n in range(N):
            if white_board[n][m] == 2:
                col += 1
        if col > 0:
            break


    print(f"#{tc}", row, col)

