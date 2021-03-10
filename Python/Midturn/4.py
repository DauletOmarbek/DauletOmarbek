a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=int(0)
for x in range(len(a)):
    for y in range(len(a)):
        if a[x]==b[y]:
            c+=1
            b[y]=0.1
print(c)

    
