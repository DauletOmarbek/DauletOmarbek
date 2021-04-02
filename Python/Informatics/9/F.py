a=input().split()
b=int(0)
for x in range(1,len(a)-1):
    if int(a[x])>int(a[x-1]) and int(a[x])>int(a[x+1]):
        b+=1
print(b)