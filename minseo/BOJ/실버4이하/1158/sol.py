'''
백준 1158문제
원형 큐
- 자리를 재활용하기 위해 생겨난 배열

'''
import sys
from collections import deque
n,k = list(map(int,sys.stdin.readline().split()))
result = []
# 큐는 1부터 시작해야 편함
q = deque(range(1,n+1))
# 큐에 값이 있을 때만 작동
while q:
    q.rotate(-(k-1))
    result.append(q.popleft())
print("<" + ', '.join(map(str,result)) + ">")
