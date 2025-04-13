from collections import deque
maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
perm_maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]

rotated_versions = [[[[0] * 5 for _ in range(5)] for _ in range(4)] for _ in range(5)]



# 돌려놓은 부분을 캐싱
for i in range(5):
    for r in range(4):
        rotated_versions[i][r] = [row[:] for row in maze[i]]
        for _ in range(r):  # 반
            rotated_versions[i][r] = list(map(list, zip(*rotated_versions[i][r][::-1])))

dzl = [0, 0, 0, 0, 1, -1]
dxl = [0, 0, 1, -1, 0, 0]
dyl = [1, -1, 0, 0, 0, 0]

min_ans = float('inf')
def comb(perm, dires = []):
    global min_ans
    if len(dires) == 5:
        if not perm_maze[0][0][0] or not perm_maze[4][4][4]:
            return
        ans = bfs()
        if ans:
            min_ans = min(min_ans, ans)
        return
    for i in range(4):
        dires.append(i)
        perm_maze[len(dires)-1] = [row[:] for row in rotated_versions[perm[len(dires)-1]][i]]
        if not perm_maze[0][0][0]:
            dires.pop()
            continue
        comb(perm, dires)
        dires.pop()

def get_perm(perm=[]):
    if len(perm) == 5:
        comb(perm, [])
        return
    for i in range(5):
        if i not in perm:
            perm.append(i)
            get_perm(perm)
            perm.pop()

# def rotate_clockwise(dires):
#     for idx, cnt in enumerate(dires):
#         for _ in range(cnt):
#             perm_maze[idx] = list(zip(*perm_maze[idx][::-1]))

# def rotate_counterclockwise(dires):
#     for idx, cnt in enumerate(dires):
#         for _ in range(cnt):
#             perm_maze[idx] = list(zip(*perm_maze[idx]))[::-1]

def bfs():
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        z, x, y = q.popleft()
        if visited[z][x][y] >= min_ans:
            continue
        for dz, dx, dy in zip(dzl, dxl, dyl):
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5 \
                    and perm_maze[nz][nx][ny] and not visited[nz][nx][ny]:
                if nz == 4 and nx == 4 and ny == 4:
                    return visited[z][x][y]
                q.append((nz, nx, ny))
                visited[nz][nx][ny] = visited[z][x][y] + 1
    return 0

get_perm()
print(-1 if min_ans == float('inf') else min_ans)