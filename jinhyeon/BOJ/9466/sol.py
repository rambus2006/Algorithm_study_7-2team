from collections import deque
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# def bfs(i):
#     q = deque()
#     team = set()
#     q.append(i)
#     team.add(i)
#     while q:
#         num = q.popleft()
#         next_num = arr[num]
#         if next_num == i:
#             break
#         if i > next_num:
#             return 0
#         if visited[next_num] or next_num in team:
#             return 0
#         q.append(next_num)
#         team.add(next_num)
#
#     for i in team:  #팀이 됐다면
#         visited[i] = 1
#     return len(team)
#
# t = int(sys.stdin.readline().rstrip())
#
# for _ in range(t):
#     n = int(sys.stdin.readline().rstrip())
#     arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
#     visited = [0] * (n + 1)
#     cnt = 0
#     for i in range(1, n+1):
#         if visited[i]:
#             continue
#         visited[i] = 1
#         cnt += bfs(i)  #
#     print(n - cnt)


def dfs(i):
    visited[i] = 1
    path.append(i)
    next_node = arr[i]
    if not visited[next_node]:
        dfs(next_node)
    elif next_node in path:
        idx = path.index(next_node)
        result.extend(path[idx:])
    path.pop()

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            path = set()
            start_idx = i
            dfs(i)

    print(n - len(result))