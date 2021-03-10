a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list()
for item in a:
    if item in b:
        c.append(item)
c.sort()
for x in c:
    print(x , end=' ')
        

