a=int(input())
b=int(input())
c=str()
for x in range((a//2)*2+(a%2)*2,b+1,2):
    c+=str(x)+" "
print(c)