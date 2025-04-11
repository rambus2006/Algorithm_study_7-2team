import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
#############################################
## 공간복잡도 : 32412
## 시간 복잡도 : 36ms
# 주석은 dp를 통해 각 숫자로 끝나는 경우의 수를 구하는 코드
# dp = [[0] * 10 for _ in range(11)]
# result = [0, 10]
# for i in range(10):
#     dp[1][i] = 1
#
# for i in range(2, 11):
#     for j in range(i - 1, 10):
#         for k in range(0, j):
#             dp[i][j] += dp[i-1][k]
#     result.append(sum(dp[i]) + result[-1])
# pprint(dp)
# print(result)

dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 0, 1, 3, 6, 10, 15, 21, 28, 36],
     [0, 0, 0, 1, 4, 10, 20, 35, 56, 84],
     [0, 0, 0, 0, 1, 5, 15, 35, 70, 126],
     [0, 0, 0, 0, 0, 1, 6, 21, 56, 126],
     [0, 0, 0, 0, 0, 0, 1, 7, 28, 84],
     [0, 0, 0, 0, 0, 0, 0, 1, 8, 36],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

result = [0, 10, 55, 175, 385, 637, 847, 967, 1012, 1022, 1023]

def find(dp, result, temp, num):

    val = result[temp]
    output = ''
    idx = 9
    for i in range(temp, 0, -1):
        for j in range(idx, -1, -1):
            if val - dp[i][j] < num:
                output += str(j)
                idx = j - 1
                break

            val -= dp[i][j]

    return output
num = int(input()) + 1
temp = 0
if num <= 1023:
    for i in range(1, len(result)):
        if result[i] >= num:
            temp = i
            break

    print(find(dp, result, temp, num))
else:
    print(-1)