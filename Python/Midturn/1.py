a=list(map(int,input().split(':')))
b=a[0]+a[1]*31+a[2]*372
if 1299*372<b and b<1922*372:
    print("YES")
else:
    print("NO")