from collections import deque  # BFS를 위한 deque 라이브러리 불러오기

T = int(input())  # 테스트 케이스의 개수를 입력받음

# 네 방향(상, 하, 좌, 우)을 탐색하기 위한 리스트
dx = [-1, 1, 0, 0]  # x축 이동: 위(-1), 아래(+1)
dy = [0, 0, -1, 1]  # y축 이동: 왼쪽(-1), 오른쪽(+1)

# BFS 함수 정의: 배추가 심어진 위치 (a, b)에서 연결된 배추들을 모두 탐색
def bfs(a, b):
    q = deque()
    q.append((a, b))  # 시작 위치 큐에 추가
    # 0 은 배추가 없으니까 탐색을 안하는데, 이때 방문한 배추를 0으로 바꿔주면 굳이 다시 탐색을 안하는구나 
    array[a][b] = 0   # 방문한 배추는 0으로 처리 (방문 표시)

    while q:  # 큐가 빌 때까지 반복
        x, y = q.popleft()  # 현재 위치 꺼내기

        for i in range(4):  # 네 방향으로 이동 시도
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고, 아직 배추가 심어져 있는 경우
            if 0 <= nx < m and 0 <= ny < n:
                if array[nx][ny] == 1:
                    q.append((nx, ny))    # 다음 위치 큐에 추가
                    array[nx][ny] = 0     # 방문 처리

# 테스트 케이스 수만큼 반복
for i in range(T):
    m, n, k = map(int, input().split())  # m: 가로, n: 세로, k: 배추 개수
    array = [[0] * n for _ in range(m)]  # 밭 정보를 저장할 2차원 배열 초기화

    # 배추가 심어진 위치에 1 표시
    for j in range(k):
        x, y = map(int, input().split())
        array[x][y] = 1

    total = 0  # 필요한 지렁이 수 (배추 무리 개수)
    for i in range(m):
        for j in range(n):
            if array[i][j] == 1:  # 아직 방문하지 않은 배추가 있으면
                bfs(i, j)         # 해당 배추를 기준으로 BFS 실행
                total += 1        # 배추 무리 수 증가

    print(total)  # 결과 출력
