x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if x1>0 and x1<9 and x2>0 and x2<9 and y1>0 and y1<9 and y2>0 and y2<9:
    if x1+2==x2:
        if y1+1==y2 or y1-1==y2:
            print("YES")
            exit()
    if x1-2==x2:
        if y1+1==y2 or y1-1==y2:
            print("YES")
            exit()
    if y1+2==y2:
        if x1+1==x2 or x1-1==x2:
            print("YES")
            exit()
    if y1-2==y2:
        if x1+1==x2 or x1-1==x2:
            print("YES")
            exit()
print("NO")