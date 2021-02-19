b=float(input())
a=str(b)
for x in range(0,len(a)):
    if a[x]==".":
        if int(a[x+1])>0 and int(a[x+1])<5:
            print(int(b))
        else:
            print(int(b)+1)