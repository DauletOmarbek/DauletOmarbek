a=int(input())
b=pow(10,a)
c=str()
for x in range(b-1,0,-2):
    c+=str(x)+" "
print(c)