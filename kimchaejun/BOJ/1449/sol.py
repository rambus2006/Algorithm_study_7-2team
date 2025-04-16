N, L = map(int, input().split())
repair_point = sorted(list(map(int, input().split())))
i, res = 0, 0
while i < N:
    std = repair_point[i]
    res += 1
    while i < N and repair_point[i] < std + L:
        i += 1
print(res)
