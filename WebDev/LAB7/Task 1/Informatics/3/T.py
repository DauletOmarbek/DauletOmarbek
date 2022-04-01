n=int(input())
a=int(0)
b=int(0)
c=int(0)
while n>0:
    if n>34:
        c+=1
        n-=60
    if 8<n and n<35:
        b+=1
        n-=10
    if n<9 and n>0 :
        a+=1
        n-=1
print(a, b, c)
