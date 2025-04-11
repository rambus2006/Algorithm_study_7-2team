def findResult(R, C, N, grid):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]


    def explode(map):
        newMap = [['O'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if map[i][j] == 'O':
                    newMap[i][j] = '.'
                    for d in range(4):
                        ni, nj = i + dx[d], j + dy[d]
                        if 0 <= ni < R and 0 <= nj < C:
                            newMap[ni][nj] = '.'
        return newMap

    if N == 1:
        return [''.join(row) for row in grid]
    elif N % 2 == 0:
        return ['O' * C for _ in range(R)]
    else:
        first = explode(grid)
    if (N - 3) % 4 == 0:
        return [''.join(row) for row in first]
    else:
        second = explode(first)
        return [''.join(row) for row in second]


R, C, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

result = findResult(R, C, N, grid)

for row in result:
    print(row)
