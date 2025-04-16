from collections import deque

def findResult(n):
    queue = deque(range(1, n + 1))
    
    while len(queue) > 1:
        queue.popleft()
        second = queue.popleft()
        
        queue.append(second)
    
    return queue[0]

n = int(input())
print(findResult(n))
