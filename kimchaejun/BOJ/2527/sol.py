for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = list(map(int, input().split()))
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')
    elif (p1 == x2 and q1 == y2) or (p2 == x1 and q2 == y1) or (p1 == x2 and q2 == y1) or (p2 == x1 and q1 == y2):
        print('c')
    elif p1 == x2 or p2 == x1 or q1 == y2 or q2 == y1:
        print('b')
    else:
        print('a')
