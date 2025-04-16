dx = [-1, -1, -1, 0, 1, 1, 1, 0] 
dy = [-1, 0, 1, 1, 1, 0, -1, -1] 

def findresult(n, arr):
    result = [['0'] * n for _ in range(n)]  
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != '.':  
                result[i][j] = '*' 
            else: 
                count = 0  
                for k in range(8): 
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != '.':
                        count += int(arr[nx][ny])
                         
                
                if count >= 10:  
                    result[i][j] = 'M'
                else:  
                    result[i][j] = str(count)

    return result

n = int(input()) 
arr = [input().strip() for _ in range(n)] 
result = findresult(n, arr)

for row in result:
    print(''.join(row)) 
