import sys

n = int(sys.stdin.readline())
coord = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

coord.sort(key=lambda x: (x[0], x[1]))


for x,y in coord:
    print(x,y)

