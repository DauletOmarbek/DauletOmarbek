a=input().split()
if len(a[1])==2 and len(a[2])==2:
    b=int(a[0])*372+int(a[1])*31+int(a[2])
    if b>1299*372 and b<1923*372:
        print("YES")
    else:
        print("NO")
else:
    print("NO") 