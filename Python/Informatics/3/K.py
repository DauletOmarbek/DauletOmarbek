x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if x1>0 and x1<9 and x2>0 and x2<9 and y1>0 and y1<9 and y2>0 and y2<9:
    for x in range(1,8):
        if x1+x==x2 and y1+x==y2 and x1+x>0 and x1+x<9 and y1+x>0 and y1+x<9:
            print("YES")
            exit()
        elif x1+x==x2 and y1-x==y2 and x1+x>0 and x1-x<9 and y1+x>0 and y1-x<9:
            print("YES")
            exit()
        elif x1-x==x2 and y1+x==y2 and x1-x>0 and x1+x<9 and y1-x>0 and y1+x<9:
            print("YES")
            exit()
        elif x1-x==x2 and y1-x==y2 and x1-x>0 and x1-x<9 and y1-x>0 and y1-x<9:
            print("YES")
            exit()
print("NO")
    
