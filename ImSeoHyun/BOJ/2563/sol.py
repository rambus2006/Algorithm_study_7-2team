T = int(input())
inputArr = []
for _ in range(T):
    inputArr.append(list(map(int,input().split())))



arr = [[0] * 100 for _ in range(100)]  

for x, y in inputArr: 
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1  



area = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            area += 1

print(area)
