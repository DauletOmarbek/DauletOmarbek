a=input().split()
b=int(a[0])
i=int(0)
for x in range(0,len(a)):
    if int(a[x])>b:
        b=int(a[x])
        i=x
print(b,i)