n = int(input())

sumnum = 0
count = 0
for i in range(1,n+1):
    sumnum += i
    if sumnum > n:
        break
    count +=1

print(count)