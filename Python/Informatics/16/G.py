a=int(input())
b=set()   #TRUE
c=set()   #FALSE
d=str(input())
while d!="HELP":
    e=set()
    e=d.split()
    answer=input()
    if answer=="YES":
        if len(b)==0:
            b.update(e)
        else:
            b=b.intersection(e)
    if answer=="NO":
        c.update(e)
    d=str(input())

for x in c:
    if x in b:
        b.remove(x)
l=set()
for y in b:
    if int(y)>a or int(y)<1:
        l.add(y)
for x in l:
    if x in b:
        b.remove(x)      
        
k=list()
for x in b:
    k.append(int(x))
k.sort()
for x in k:
    print(x,end=" ")






