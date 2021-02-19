a=input().split()
b=str()
for x in range(len(a)-1,-1,-1):
    b+=a[x]+" "
print(b)