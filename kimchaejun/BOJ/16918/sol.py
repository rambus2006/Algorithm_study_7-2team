import sys
N, M, TIMER = map(int, sys.stdin.readline().split())
bomb_set = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
target_bomb = 'O'
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def explosion(target):
    to_clear = []
    for ei in range(N):
        for ej in range(M):
            if bomb_set[ei][ej] == target:
                to_clear.append((ei, ej))
    for ei, ej in to_clear:
        bomb_set[ei][ej] = '.'
        for dx, dy in dxy:
            ni, nj = ei + dx, ej + dy
            if 0 <= ni < N and 0 <= nj < M and bomb_set[ni][nj] != target:
                bomb_set[ni][nj] = '.'


for t in range(1, TIMER+1):
    if t % 2 == 0:
        for i in range(N):
            if target_bomb == 'O':
                bomb_set[i] = ['N' if bomb_set[i][j] == '.' else bomb_set[i][j] for j in range(M)]
            else:
                bomb_set[i] = ['O' if bomb_set[i][j] == '.' else bomb_set[i][j] for j in range(M)]
        target_bomb = 'N' if target_bomb == 'O' else 'O'
    else:
        if t >= 3:
            explosion_target = 'N' if target_bomb == 'O' else 'O'
            explosion(explosion_target)

for i in range(N):
    print(''.join(bomb_set[i]).replace('N', 'O'))
