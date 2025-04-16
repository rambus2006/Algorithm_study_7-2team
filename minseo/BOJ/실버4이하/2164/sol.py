from collections import deque

n = int(input())
# 길이 만큼의 큐를 만들어준다.
queue = deque(range(1,n+1))

while len(queue) > 1:
    # 우선 맨 앞의 큐를 제거한다.
    queue.popleft()
    # 그 다음의 pop한 값을 큐에 추가하여 끝부분에 추가한다.
    queue.append(queue.popleft())

    #계속 pop하고 뒤로 보내다 보면 queue[0]하나만 남게 된다.
print(queue[0])