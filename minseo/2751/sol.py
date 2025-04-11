import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
for num in sorted(arr):
    print(num)
'''
import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

sys.stdout.write('\n'.join(map(str, arr)) + '\n')

'''