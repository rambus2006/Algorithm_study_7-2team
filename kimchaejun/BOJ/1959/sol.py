import sys
M, N = map(int, sys.stdin.readline().split())
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
wall = [N, M, 1, 1]
x, y, order, order_cnt = 1, 1, 0, 0
K = N * M + 1
while True:
    if order == 0:
        move_cnt = wall[order] - y
    elif order == 1:
        move_cnt = wall[order] - x
    elif order == 2:
        move_cnt = y - wall[order]
    else:
        move_cnt = x - wall[order]
    if K <= move_cnt:
        x += dxy[order][0] * K
        y += dxy[order][1] * K
        break
    else:
        x += dxy[order][0] * move_cnt
        y += dxy[order][1] * move_cnt
        K -= move_cnt
        wall[order] = wall[order] - 1 if order < 2 else wall[order] + 1
        order = (order + 1) % 4
        order_cnt += 1
print(order_cnt)
print(x, y)