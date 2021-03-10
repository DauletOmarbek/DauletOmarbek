a=list(map(int,input().split()))
aniy=list()
bory=list()
for x in range(a[0]):
    c=int(input())
    aniy.append(c)
for x in range(a[1]):
    c=int(input())
    bory.append(c)
n=int(0)
equal=list()

for color in aniy:
    if color in bory:
        n+=1
        equal.append(color)
print(n)
for x in equal:
    print(x,end=" ")
print(" ")

print(abs(len(aniy)-n))
for item in equal:
    if item in aniy:
        aniy.remove(item)
    if item in bory:
        bory.remove(item)
aniy.sort()
bory.sort()

for x in aniy:
    print(x , end=" ")

print(" ")
print(abs(len(bory)-n))
for x in bory:
    print(x , end=' ')