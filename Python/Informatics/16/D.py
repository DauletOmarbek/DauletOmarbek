a=input().split()
b=set()
b.add(a[0])
print("NO")
for x in range(1,len(a)):
    if a[x] in b:
        print("YES")
    else:
        print("NO")
    b.add(a[x])

