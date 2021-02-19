a=input().split()
b=int(input())
c=str()
if b>0:
    for x in range(b-1,len(a)):
        c+=a[x]+" "
    for x in range(b-1):
        c+=a[x]+" "
else:
    for x in range(b,len(a)+b):
        c+=a[x]+" "
    
print(c)