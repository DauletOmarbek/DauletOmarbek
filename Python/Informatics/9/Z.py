a=input().split()
b=int(input())
c=str()
d=3%len(a)
for x in range(d,len(a)):
    c+=a[x]+" "
for x in range(d):
    c+=a[x]+" "
print(c)