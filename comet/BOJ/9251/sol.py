import sys
sys.stdin = open("input.txt", "r")
#############################################
def find():
    first = input().strip()
    second = input().strip()
    if len(first) < len(second):
        first, second = second, first
    dp = [0] * len(first)
    cursor = 0

    for i in range(len(first)):
        for j in range(cursor, len(second)):




print(find())