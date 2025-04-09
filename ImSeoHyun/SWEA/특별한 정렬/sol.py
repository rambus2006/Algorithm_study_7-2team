def findResult():
    result = []
    flag = 0
    while arr:
        if not flag:
            result.append(str(arr.pop()))
            flag = 1
        else:
            result.append(str(arr.pop(0)))
            flag = 0
    return result[:10]


T = int(input())

for tc in range(1, T + 1): 
    n = int(input())
    arr = list(map(int ,input().split())) 
    arr.sort()
    print(f'#{tc} ' + ' '.join(findResult()))