a=int(input())
b=int(input())
if (b==0 and a==0):
    print("INF")
    exit()
if a==0:
    print("NO")
    exit()
    
if (-1*b)%a!=0:
    print("NO")
    exit()

if (-1*b)%a==0:
    print(int((-1*b)/a)) 
    exit()

