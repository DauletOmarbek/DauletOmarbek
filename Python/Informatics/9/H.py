a=input().split()
b=int(int(1000))
for x in range(len(a)):
    if int(a[x])>0:
        if b>int(a[x]):
            b=int(a[x])
print(b)