a=list()
b=list()
for x in range(3):
    c=int(input())
    a.append(c)

for x in range(3):
    c=int(input())
    b.append(c)
a.sort()
b.sort()
if a[0]==b[0] and a[1]==b[1] and a[2]==b[2]:
    print("Boxes are equal")
    exit()
if a[0]<=b[0] and a[1]<=b[1] and a[2]<=b[2]:
    print("The first box is smaller than the second one")
    exit()
if a[0]>=b[0] and a[1]>=b[1] and a[2]>=b[2]:
    print("The first box is larger than the second one")
    exit()
else:
    print("Boxes are incomparable")
    exit()