a=int(input())
everyone=set()
every=set()
for x in range(a):
    b=int(input())
    c=set()
    for y in range(b):
        d=str(input())
        c.add(d)
    if len(everyone)==0:
        everyone.update(c)
    else:
        everyone=everyone.intersection(c)
    if len(every)<len(c):
        every=c

g=list()
f=list()

for x in everyone:
    g.append(x)

for x in every:
    f.append(x)



print(len(everyone))
for x in g:
    print(x)

print(len(every))
for x in f:
    print(x)