a=input().split()
for x in range(1,len(a)):
    if (int(a[x])>=0 and int(a[x-1])>=0) or (int(a[x])<0 and int(a[x-1])<0):
        print(a[x-1], a[x])
        exit()
