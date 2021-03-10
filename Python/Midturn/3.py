a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=int(input())
d=int(0)
for x in range(len(a)):
    if a[x]<b[x]:
        if a[x]<c and c<b[x]:
            d+=1
    if a[x]>b[x]:
        if b[x]<c and c<a[x]:
            d+=1


print(d)
