a=int(input())
b=int(input())
c=str()
if a<b:
    for x in range(a,b+1):
        c+=str(x)+" "  
    print(c)
    
else:
    for x in range(a,b-1,-1):
        c+=str(x)+" "  
    print(c)