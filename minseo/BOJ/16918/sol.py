'''
0초 후(1초)
격자판에 visited = 0으로 설정
초기상태에서 폭탄이 있으면 1로 설정

--> 여기로 다시 돌아가기
1초 후(2초)
모든칸에 폭탄 설치 (visited +=1 )

2초 후(3초)
visited += 1 모든칸 더해준다. -> 반복
이때 visited==3이 있으면 델타 탐색하기
델타 탐색 해서 (4방향씩 1칸),
visited = 0 으로 바꾸기
배열에 저장
만약 맨 처음 배열과 같은 배열이면 멈추기
배열의 길이 세기
N % 배열의 길이 = 나머지
나머지 위치의 배열에서 값을 가져오기
배열의 값을 비교-> 1이상이면 0,0이면 . 로 출력

배열이 결국에 다 같은 곳에서 터지잖아요.
0 초 - 1
1초 - 2
2초 - 3 <- 터져서 0
3초 - 1
4초 -2
5초 -3 <-터져서 0
6초 - 1
7초 - 2
8초 - 3 <- 터져서 
import sys

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def GetDelta():
    for i in range(row):
        for j in range(col):

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx <= row and 0 <= ny <= col:
                    grid[nx][ny] = 'O'

row,col,n = list(map(int,sys.stdin.readline().split()))
grid = [list(sys.stdin.readline().rstrip()) for _ in range(row)]

0초 후(1초)
격자판에 visited = 0으로 설정
초기상태에서 폭탄이 있으면 1로 설정

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(row):
    for j in range(col):
        # 일단 처음에 . 과 O으로 된 배열을숫자 count 할 수 있는 배열로 만들어주기
        if grid[i][j] == 'O':
            countgrid[i][j] = 1
initcountgrid = countgrid


gridsave = dict()
cnt = 1
gridsave[cnt] = initcountgrid
while True:
    cnt +=1
    for i in range(row):
        for j in range(col):
            #여기 부분만 반복된다.
            countgrid[i][j] += 1
            # 3인 경우
            if countgrid[i][j] == 3:
                for k in range(4):
                    #델타 탐색
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx <= row and 0 <= ny <= col:
                        countgrid[nx][ny] = 0
                    # 3이 없는 경우 다시 돌아가 실행한다
    gridsave[cnt] = countgrid
    if countgrid == initcountgrid:
        break
#for u in gridsave[n % len(gridsave)]:
print(gridsave)
'''

R, C, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

# 2초에 전부 폭탄 채운 상태
allO = [['O'] * C for _ in range(R)]

# 3초에 폭탄 터뜨린 상태 만들기
boom1 = [['O'] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'O':
            boom1[i][j] = '.'  # 자기 자신 터짐
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < R and 0 <= nj < C:
                    boom1[ni][nj] = '.'

# 5초에 또 터짐 (boom1 기준으로)
boom2 = [['O'] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if boom1[i][j] == 'O':
            boom2[i][j] = '.'
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < R and 0 <= nj < C:
                    boom2[ni][nj] = '.'

# 시간에 따라 어떤 결과 보여줄지 고름
if N == 1:
    for i in range(R):
        print(''.join(grid[i]))  # 그냥 입력 그대로 출력
elif N % 2 == 0:
    for i in range(R):
        print(''.join(allO[i]))  # 전부 O
elif (N - 3) % 4 == 0:
    for i in range(R):
        print(''.join(boom1[i]))  # 3초 상태 반복
else:
    for i in range(R):
        print(''.join(boom2[i]))  # 5초 상태 반복


