a=int(input())
b=int(input())
c=int(input())
d=int(input())
for x in range(1001):
    if a*(pow(x,3))+b*(pow(x,2))+c*x+d==0:
        print(x)