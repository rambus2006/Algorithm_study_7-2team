"""

N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 수) 와 같다.


"""

N = int(input())
count = 0
num = 665

while True:
    num += 1
    if '666' in str(num):
        count += 1
        if count == N:
            print(num)
            break
