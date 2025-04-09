def hanoitop(start_rod, end_rod, i, num):
    #시작 장대, 움직일 장대, 목표값의 인덱스(몇 층), 목표 값
    if start_rod == 3 and end_rod == 3:
        print('here')
    global ans
    if rod[start_rod][-1] != num: # 맨위가 목표한 숫자가 아니면
        for idx in range(1, 4):
            if idx not in [start_rod, end_rod]:
                hanoitop(start_rod, idx, i + 1, rod[start_rod][i + 1])   # 나머지를 다른 곳에 두고
    if rod[end_rod] and rod[end_rod][-1] < num:  #둘 곳에 수가 더 크면
        for idx in range(1, 4):
            if idx not in [start_rod, end_rod]:
                hanoitop(end_rod, idx, len(rod[end_rod])-1, rod[end_rod][len(rod[end_rod])-1])
    rod[end_rod].append(rod[start_rod].pop())   # 목표한 수를 목표한 곳에 둔다
    # 둘떄 기록
    print(rod)
    print(start_rod, end_rod)
    ans.append((start_rod, end_rod))

k = int(input())
ans = []
len_res = float('inf')
rod = [[] for _ in range(4)]
rod[1] = list(range(k, 0, -1))
print(rod)
min_cnt = float('inf')

for i in range(k+1, 0, -1):
    for j in range(1, 4):
        for k in range(len(rod[j])):
                if rod[j][k] == i:
                    hanoitop(j, 3, k, i)
                    break


print(ans)
