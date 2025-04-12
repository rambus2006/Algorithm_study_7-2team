import sys
sys.stdin = open("input.txt", "r")

T= int(input())
for tc in range(1, T+1):
    N = int(input()) #당근의 개수
    karrot = list(map(int, input().split())) # 당근 크기
    karrot.sort()

    result = 9999999999
    for i in range(1, N-1):
        for j in range(i +1, N):
            if karrot[i - 1] == karrot[i] or karrot[j - 1] == karrot[j]:
                continue

            s = i
            m = j - i
            l = N - j

            min_k = min(s, m, l)
            max_k = max(s, m, l)

            diff = max_k - min_k
            result = min(result, diff)

    if result == 9999999999:
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', result)