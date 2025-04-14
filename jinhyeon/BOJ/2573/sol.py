from collections import deque
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dxl = [0, 1, 0, -1]
dyl = [1, 0, -1, 0]

ans = 0
while True: # 두 덩어리 이상 쪼개질 때 까
    # 1. 모든 빙산 새고 queue에 삽입 - 빙산 개수 세
    # 2. queue 빠져나가면서 visited 배열에 빙산 개수 할당
    # 3. visited 배열 돌면서 빙산 --
    # 4. 빙산 bfs() 탐색 후 첫 빙산 개수와 다르면 break   < 틀림
    visited = [[-1] * m for _ in range(n)]  # 주변에 바닷물 개수를 세기도 하는 배열이기에 -1로 초기화  -1 미방문 0 방
    ans += 1
    q = deque()

    found = False
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                q.append((i, j))
                found = True
                break
        if found:
            break

    while q:
        x, y = q.popleft()
        water_cnt = 0  # 주변 물 개수
        for dx, dy in zip(dxl, dyl):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if arr[nx][ny] <= 0: # 물이면
                water_cnt += 1
                continue
            if visited[nx][ny] == -1: # 방문 안했으면
                q.append((nx, ny))
                visited[nx][ny] = 0 #방문 처리
        visited[x][y] = water_cnt

    broken_ice = False
    for i in range(n):
        for j in range(m):
            if visited[i][j] != -1:
                arr[i][j] -= visited[i][j]
                visited[i][j] = -1
            else:
                if arr[i][j] > 0:
                    broken_ice = True
                    break
        if broken_ice:
            break

    if broken_ice and ans == 1:
        ans = 0
        break
    flag = False
    ice_flag = False
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                if flag and visited[i][j] == -1:
                    ice_flag = True
                    break
                flag = True
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for dx, dy in zip(dxl, dyl):
                        nx, ny = x + dx, y + dy
                        if not (0 <= nx < n and 0 <= ny < m):
                            continue
                        if arr[nx][ny] > 0 and visited[nx][ny] == -1:  # 방문 안했으면
                            q.append((nx, ny))
                            visited[nx][ny] = 0  # 방문 처리
    if not flag:    # 빙산이 모두 녹았을 때 덩어리로 분리 되지 않다면
        ans = 0
        break
    if ice_flag:    # 덩어리가 나누어졌을
        break

print(ans)
