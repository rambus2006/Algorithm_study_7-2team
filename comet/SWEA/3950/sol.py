import sys
sys.stdin = open("input.txt", "r")
#############################################
def r_operation(left, right, string):
    string = list(string)
    string[left:right + 1] = string[left:right + 1][::-1]
    for i in range(left, right + 1):
        if string[i] == '(':
            string[i] = ')'
        elif string[i] == ')':
            string[i] = '('
    return ''.join(string)

def flip(string):
    global flip_cnt, result
    min_value = 0
    pos = -1
    total = 0
    for i in range(len(string)):
        if string[i] == '(':
            total += 1
        elif string[i] == ')':
            total -= 1

        if total < min_value:
            min_value = total
            pos = i

    if pos != -1:
        flip_cnt += 1
        result.append((0, pos))
        string = r_operation(0, pos, string)
    return string

def solve(string):
    global flip_cnt, result, sub_sum_arr
    n = len(string)
    if n % 2 == 1:
        flip_cnt = -1
        return

    string = flip(string)

    sub_sum_arr = []
    total = 0
    for ch in string:
        if ch == '(':
            total += 1
        elif ch == ')':
            total -= 1
        sub_sum_arr.append(total)

    if sub_sum_arr[-1] == 0:
        return

    half_value = sub_sum_arr[-1] // 2
    pos = -1
    for i in range(n):
        if sub_sum_arr[i] == half_value:
            pos = i + 1

    result.append((pos, n - 1))
    flip_cnt += 1



tc = int(input())
for tc in range(1, tc + 1):

    length = int(input())
    string = input()
    flip_cnt = 0
    result = []
    sub_sum_arr = []

    solve(string)

    print(f"#{tc} {flip_cnt}")
    for start, end in result:
        print(f"{start} {end}")
