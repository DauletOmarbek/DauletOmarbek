s=input()
c=input()
d=int(0)
f=list()
a=list()
for x in range(len(s)):
    if s[x]==c:
        d+=1
        f.append(x)

for x in range(len(s)):
    b=int(len(s))
    for y in range(d):
        if abs(int(f[y])-x)<b:
            b=abs(int(f[y])-x)
    a.append(b)
        
print(a)