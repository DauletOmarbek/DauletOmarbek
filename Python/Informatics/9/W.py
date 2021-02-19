a=input().split()
b=str()
c=int(0)
for x in range(len(a)):
    if int(a[x])>0:
        b+=str(a[x])+" "
        c+=1
for x in range(len(a)-c):
    b+=str(0)+" "
print(b)
