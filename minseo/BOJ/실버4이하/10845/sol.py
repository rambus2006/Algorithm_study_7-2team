'''
< 큐 개념 정리 >
{ 큐 }
- 큐는 FIFO 구조 (뒤로 들어가면 앞으로 나오는 구조)
- 줄서기,
{ 큐 연산 종류 }
- EnQueue() : 큐의 뒤쪽에 원소를 삽입하는 연산
- Dequeue() : 큐의 앞쪽에서 원소를 삭제하고 반환
- IsEmpty() : 큐가 공백상태인지 확인하는 연산
- IsFull() : 큐가 포화상태인지 확인하는 연산
- peek() : 큐의 앞쪽에서 원소를 삭제없이 반환하는 연산

>문제 분석
- push(x) : 정수 x 를 큐에 넣는 연산
- pop(): 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐가 들어있지 않으면
-1을 출력한다.
- size() : 큐가 들어있는 정수의 개수를 출력한다.
'''
from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
queue = deque()
for _ in range(n):
    message = sys.stdin.readline().rstrip().split()
    if message[0] == 'push':
        queue.append(message[1])
    if message[0] == 'pop':
        print(queue.popleft() if queue else -1)
    if message[0] == 'size':
        print(len(queue))
    if message[0] == 'empty':
        print(1 if not queue else 0)
    if message[0] == 'front':
        print(queue[0] if queue else -1)
    if message[0] == 'back':
        print(queue[-1] if queue else -1)