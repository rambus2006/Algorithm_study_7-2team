import sys
sys.stdin = open("input.txt", "r")
#############################################
from collections import deque
def bfs(y, x, visited, arr):
    standard = arr[y][x]
    que = deque([(y, x)])
    visited[y][x] = 1
    result = [(y, x)]
    while que:
        cur_y, cur_x = que.popleft()

        for dy, dx in direc:
            tempy = cur_y + dy
            tempx = cur_x + dx
            if 0 <= tempy < width and 0 <= tempx < length and not visited[tempy][tempx] and arr[tempy][tempx] == standard:
                visited[tempy][tempx] = 1
                que.append((tempy, tempx))
                result.append((tempy, tempx))
    if len(result) >= 4:
        return result
    return

def drop(y, x, arr):
    if arr[y+1][x] != '.':
        return
    dy, dx = y, x
    while dy < width - 1:
        dy += 1
        if arr[dy][dx] != '.':
            arr[y][x], arr[dy-1][dx] = arr[dy-1][dx], arr[y][x]
            return
        elif dy == width - 1:
            arr[y][x], arr[dy][dx] = arr[dy][dx], arr[y][x]
            return
    return




def find():

    arr = [list(input().strip()) for _ in range(width)]
    cnt = 0

    while 1:
        visited = [[0] * length for _ in range(width)]
        boom = []
        for i in range(width):
            for j in range(length):
                if not visited[i][j] and arr[i][j] != '.':
                    val = bfs(i, j, visited, arr)
                    if val:
                        boom += val

        if not boom:
            return cnt
        else:
            for y, x in boom:
                arr[y][x] = '.'
        for i in range(width - 2, -1, -1):
            for j in range(length - 1, -1, -1):
                if arr[i][j] != '.':
                    drop(i, j, arr)


        cnt += 1

width = 12
length = 6
direc = (1, 0), (0, 1), (-1, 0), (0, -1)
print(find())