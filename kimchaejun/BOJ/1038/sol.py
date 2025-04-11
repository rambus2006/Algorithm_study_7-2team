import sys
N = int(sys.stdin.readline())
nums = list(range(9, -1, -1))
cnt, res = 0, [0]
for i in range(1, 1024):
    tmp = ''
    for j in range(10):
        if i & (1 << j):
            tmp += str(nums[j])
    res.append(int(tmp))
res = sorted(list(set(res)))
print(res[N] if N < len(res) else -1)
