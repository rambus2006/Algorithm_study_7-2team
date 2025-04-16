'''
미로 탐색
n * m 짜리 미로

'''
from collections import deque

n,m = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 방문 기록 및 거리 저장
queue = deque()
queue.append((0,0))
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<= ny <m:
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
print(maze[n-1][m-1])
