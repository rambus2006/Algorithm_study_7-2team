'''


'''
# bfs는 deque 사용
from collections import deque

n,m = map(int,input().split())
# 종이
paper = [list(map(int,input().split())) for _ in range(n)]
# 방문 확인 배열
visited = [[False] * m for _ in range(n)]
result = []
# 4방향 탐색용 배열
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    #들어왔다 == 1이다. 이므로 현재 자신을 세어준다.
    count = 1
    #bfs 함수를 실행할 때 큐를 생성
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        # 상하좌우로 움직인다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위 안에 있고, 방문을 안한 경우
            if 0<= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and paper[nx][ny] == 1:
                    count +=1
                    visited[nx][ny] = True
                    queue.append([nx,ny])
    return count

# 열
for x in range(n):
    # 행
    for y in range(m):
        if paper[x][y] == 1 and visited[x][y] == False:
            visited[x][y] = True
            pic = bfs(x,y)
            result.append(pic)
if len(result) == 0:
    print(len(result))
    print(0)
else:
    print(len(result))
    print(max(result))