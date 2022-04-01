x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if x1>0 and x1<9 and x2>0 and x2<9 and y1>0 and y1<9 and y2>0 and y2<9:
    if (x1+y1)%2==(x2+y2)%2:
        print("YES")
    else:
        print("NO")