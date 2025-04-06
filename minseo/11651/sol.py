'''
> 입력값
6
0 4
1 2
1 -1
2 2
3 3
4 3
> 문제 분석
- 좌표값 정리
- y 순으로 증가(오름차순)
- 만약 y좌표가 같은 경우라면
    - x 좌표가 작은거 -> 큰거로 정렬
- 리스트 출력
if coord[0][idx] == coord[0][idx+1]:
        if coord[idx][0] > coord[idx + 1][0]:
            coord[0],coord[1] = coord[1],coord[0]
    if idx + 1 == n:
        break
    if coord[0][idx] > coord[0][idx+1]:
        coord[0],coord[1] = coord[1],coord[0]
'''
import sys

# 입력 받기
coord = []
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    x,y = sys.stdin.readline().rstrip().split()
    coord.append((int(x),int(y)))

coord.sort(key=lambda c:(c[1],c[0]))

for x,y in coord:
    print(x,y)


