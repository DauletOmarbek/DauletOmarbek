a=input().split()
for x in range(1,len(a)):
    if len(a[x])<=len(a[x-1]):
        print("NO")
        exit()
print("YES")
