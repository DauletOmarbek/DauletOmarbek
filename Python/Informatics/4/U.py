a=int(input())
b=int(input())
for x in range(a,b+1):
    c=str(x)
    if c[0]==c[3] and c[1]==c[2]:
        print(x)