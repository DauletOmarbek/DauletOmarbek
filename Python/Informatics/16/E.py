a=list(map(int,input().split()))
aniy=set()
bory=set()
for x in range(a[0]):
    c=int(input())
    aniy.add(c)
for x in range(a[1]):
    c=int(input())
    bory.add(c)

sorted(aniy,key=int)
sorted(bory,key=int)
c=set()
c=aniy.intersection(bory)
print(len(c))
for x in c:
    print(x,end=" ")
    aniy.remove(x)
    bory.remove(x)
print(" ")
print(len(aniy))
for x in aniy:
    print(x,end=" ")
print(" ")
print(len(bory))
for x in bory:
    print(x,end=" ")