import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dxy = [[0, -1], [0, 1], [1, 0], [-1, 0]]
def view_rgb(start_x, start_y, rgb):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != 1:
                if rgb == matrix[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1


def change_rgb():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'R':
                matrix[i][j] = 'G'


N = int(input())
matrix = [list(map(str, input().strip())) for _ in range(N)]
visited = [[0]* N for _ in range(N)]
result = 0
result2 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            view_rgb(i, j, matrix[i][j])
            result += 1

change_rgb()

visited = [[0]* N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            view_rgb(i, j, matrix[i][j])
            result2 += 1

print(result,result2)
