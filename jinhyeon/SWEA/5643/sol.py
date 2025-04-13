from collections import deque
T = int(input())
def bfs(idx):
    visited = [0] * (n+1)
    q = deque()
    q.append(idx)
    cnt[idx] += 1
    visited[idx] = 1
    val = 0
    while q:
        d = q.popleft()
        for i in node.get(d,[]):
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt[i] += 1
                val += 1
    cnt[idx] += val

for tc in range(1,T + 1):
    n = int(input())
    m = int(input())
    node = {}
    visited = [0] * (n+1)
    cnt = [0] * (n+1)
    ans = 0
    for _ in range(m):
        k, v = map(int, input().split())
        node.setdefault(k, []).append(v)
    for i in range(1,n+1):
        bfs(i)
    for i in cnt:
        if i == n:
            ans += 1
    print(f'#{tc} {ans}')