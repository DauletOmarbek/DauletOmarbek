a=int(input())
b=int(0)
c=str()
for x in range(2,a+1):
    b+=(x-1)*x
    c+=str(x-1)+"*"+str(x)
    if x!=a:
        c+="+"
    else :
        c+="="

print(c+str(b))