import heapq
import sys

N = int(sys.stdin.readline().rstrip())

h = []
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    heapq.heappush(h, num)

while h:
    print(heapq.heappop(h))