import sys
sys.stdin = open("input.txt", "r")

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    """
    a - 겹침
    b - 선으로 겹침
    c - 점으로 겹침
    d - 안 겹침
    """

    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')

    elif (x2 == p1 and y2 == q1) or (x2 == p1 and y1 == q2) or (x1 == p2 and y1 == q2) or (x1 == p2 and y2 == q1):
        print('c')

    elif p1 == x2 or x1 == p2 or y1 == q2 or y2 == q1:
        print('b')

    else:
        print('a')



