a=input().split()
for x in range(1,len(a)):
    if int(a[x])>int(a[x-1]):
        print(a[x],end=" A")
