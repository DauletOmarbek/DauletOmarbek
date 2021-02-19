a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(0)
for x in range(1001):
    if (a*(pow(x,3))+b*(pow(x,2))+c*x+d)==0 and x-e!=0:
        k+=1
print(k)    