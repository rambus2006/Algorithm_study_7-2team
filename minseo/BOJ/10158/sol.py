import sys

w,h = map(int,sys.stdin.readline().split())
x,y = map(int,sys.stdin.readline().split())
t = int(sys.stdin.readline().rstrip())
# x + t % (2*w)
current_x = (x + t) % (2 * w)
current_y = (y + t) % (2 * h)

if current_x > w:
    current_x = 2 * w - current_x
if current_y > h:
    current_y = 2 * h - current_y
print(current_x,current_y)