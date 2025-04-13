import sys
sys.stdin = open("input.txt", "r")
"""
'G' : RC카가 이동 가능한 땅
'T' : RC카가 이동이 불가능한 나무

'X' : 현재 RC카의 위치
'Y' : RC카를 이동 시키고자 하는 위치

RC카의 조종기로는 아래의 동작들을 할 수 있다.
'A' : 앞으로 이동 - 나무가 있는 곳이나 필드를 벗어나는 경우에는 아무 일도 일어나지 않는다.

      (RC카가 망가지는것을 방지하고자 장애물 판단 시스템이 탑재되었다.)
'L' : 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
'R' : 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전

차윤이는 RC카를 항상 위를 바라보는 방향으로 부터 조종을 시작한다.
차윤이가 RC카를 조종한 커맨드가 주어졌을 때,  목적지에 도달 할 수 있는지 구하라. 

첫번째 줄에는 테스트 케이스의 개수 T가 주어진다. (1 <= T <= 10) 
각 테스트 케이스의 첫번째 줄에 필드의 크기 N이 주어진다. (2 <= N <= 5)
두번째 줄부터 N개의 줄에 걸쳐 필드의 정보가 공백 없이 주어진다.
필드의 정보는 본문의 설명을 참고하라. 
다음 줄에는 조종을 한 횟수 Q가 주어진다. (1 <= Q <= 5)
다음 Q개의 줄에는 커맨드의 길이 C와 커맨드가 공백으로 구분되어 주어진다. (1 <= C <= 50)


RRAALAAA

1. R A L 구분해야함
2. R 인 경우 오른쪽 90도 회전
3. A 장애물 있으면 안 감
4. L 왼쪽으로 90도 회전
이거 왼 오를 어떻게 구별할것인지?
5. 이것만 해결하면 그냥 델타탐색 하면 됨
"""
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(str, input().strip())) for _ in range(N)]
    Q = int(input()) # 조종을 한 횟수
    result = []

    for _ in range(Q):
        start_x = start_y = 0
        dir = 0

        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 'X':  # 처음위치
                    start_x, start_y = i, j


        C, command = map(str, input().split())
        for r_c in command:
            if r_c == "R":
                dir = (dir + 1) % 4
            elif r_c == "L":
                dir = (dir - 1) % 4
            else:
                dx, dy = dxy[dir]
                nx = start_x + dx
                ny = start_y + dy

                if 0 <= nx < N and 0 <= ny < N:
                    if matrix[nx][ny] != 'T':
                        start_x, start_y = nx, ny


        if matrix[start_x][start_y] == 'Y':
            result.append(1)
        else:
            result.append(0)



    print(f"#{tc}", *result)