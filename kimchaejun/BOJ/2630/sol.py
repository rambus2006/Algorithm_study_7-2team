N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue, white = 0, 0


def binary_search(x, y, size):
    global blue, white
    check = sum([paper[i][j] for j in range(x, x+size) for i in range(y, y+size)])
    if check == 0:
        white += 1
    elif check == (size**2):
        blue += 1
    else:
        half = size // 2
        binary_search(x, y, half)
        binary_search(x+half, y, half)
        binary_search(x, y+half, half)
        binary_search(x+half, y+half, half)


binary_search(0, 0, N)
print(white)
print(blue)
