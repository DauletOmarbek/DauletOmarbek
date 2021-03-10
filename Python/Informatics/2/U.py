a=int(input())
b=int(input())
c=int(0)
c+=b//a
if b%a>0:
    c+=1
print(c)