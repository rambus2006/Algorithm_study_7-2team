N = int(input())
nums = list(map(int, input().split()))
std = nums[0]
low_cnt, high_cnt = 0, 0
tmp_low, tmp_high = 1, 1
for i in range(1, N):
    if nums[i] > std:
        tmp_high += 1
        if tmp_low:
            low_cnt = max(low_cnt, tmp_low)
            tmp_low = 1
    elif nums[i] < std:
        tmp_low += 1
        if tmp_high:
            high_cnt = max(high_cnt, tmp_high)
            tmp_high = 1
    else:
        tmp_low += 1
        tmp_high += 1
        low_cnt = max(low_cnt, tmp_low)
        high_cnt = max(high_cnt, tmp_high)
    std = nums[i]
low_cnt = max(low_cnt, tmp_low)
high_cnt = max(high_cnt, tmp_high)
print(max(high_cnt, low_cnt))
