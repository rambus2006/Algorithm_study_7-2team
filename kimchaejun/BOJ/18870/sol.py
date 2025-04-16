# Code 1
N = int(input())
pos = list(map(int, input().split()))
pos_compress = sorted(set(pos))
pos_dict = {}
for i in range(len(pos_compress)):
    pos_dict.setdefault(pos_compress[i], i)
pos = [str(pos_dict[p]) for p in pos]
print(' '.join(pos))

# Code 2
N = int(input())
pos = list(map(int, input().split()))
pos_compress = sorted(set(pos))
pos_dict = {v: i for i, v in enumerate(pos_compress)}
print(' '.join([str(pos_dict[p]) for p in pos]))
