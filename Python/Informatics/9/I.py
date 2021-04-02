a=input().split()
b=list()
for x in a:
    if int(x)%2==1:
        b.append(int(x))
c=int(b[x])
for x in range(1,len(b)):
    if c>b[x]:
        c=b[x]
print(c)
