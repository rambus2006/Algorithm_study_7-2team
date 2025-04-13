import sys
sys.stdin = open('sample_input (2).txt')

def dfs(idx, a, b):
    if idx == n:
        global min_val
        A = get_point(a)
        B = get_point(b)
        min_val = min(abs(A-B) // 2, min_val)
        return

    a.append(idx)
    dfs(idx + 1, a, b)
    a.pop()
    b.append(idx)
    dfs(idx + 1, a, b)
    b.pop()

def get_point(lst):
    point = 0
    for i in lst:
        for j in lst:
            if i == j:
                continue
            point += arr[i][j] + arr[j][i]
    return point

T = int(input())
for tc in range(1,T + 1):
    n = int(input())
    min_val = float('inf')
    arr = [list(map(int,input().split())) for _ in range(n)]

    dfs(0, [], [])
    print(f'#{tc} {min_val}')