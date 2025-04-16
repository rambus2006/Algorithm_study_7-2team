N = int(input())
mine = [input() for _ in range(N)]
res = [['0']*N for _ in range(N)]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
point = []
for i in range(N):
    for j in range(N):
        if mine[i][j] == '.':
            continue
        res[i][j] = '*'
        for dx, dy in dxy:
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < N and res[nx][ny] != '*' and res[nx][ny] != 'M':
                tmp = int(mine[i][j]) + int(res[nx][ny])
                res[nx][ny] = str(tmp) if tmp < 10 else 'M'
for i in range(N):
    print(''.join(res[i]))
