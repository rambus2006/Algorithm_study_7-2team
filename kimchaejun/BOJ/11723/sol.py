import sys
N = int(sys.stdin.readline())
S, res = 0, []
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'all':
        S = (1 << 20)-1
    elif order[0] == 'empty':
        S = 0
    else:
        n = int(order[1])-1
        if order[0] == 'add':
            S |= (1 << n)
        if order[0] == 'remove':
            S &= ~(1 << n)
        if order[0] == 'check':
            sys.stdout.write('1\n' if S & (1 << n) else '0\n')
        if order[0] == 'toggle':
            S ^= (1 << n)

