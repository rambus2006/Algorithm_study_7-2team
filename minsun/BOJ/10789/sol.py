"""
Aa0aPAf985Bz1EhCz2W3D1gkD6x
"""
import sys
sys.stdin = open('input.txt', 'r')

N = 5
matrix = [list(map(str, input().strip())) for _ in range(N)]

for i in range(15):
    for j in range(5):
        if i < len(matrix[j]):
            print(matrix[j][i], end="")