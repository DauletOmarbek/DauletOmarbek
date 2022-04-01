from itertools import count


n = int(input())
count = int(0)
for x in range(n):
    a = int(input())
    if a==0:
        count+=1
print(count)