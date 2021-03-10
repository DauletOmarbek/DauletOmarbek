import math
a=int(input())
b=int(input())
c=int(input())
D=math.sqrt(b*b-4*a*c)
if D<0:
    exit()
if D>0:
    print(int(min((((-1)*b+D)/2*a), (((-1)*b-D)/2*a))) , end=' ') 
    print(int(max((((-1)*b+D)/2*a), (((-1)*b-D)/2*a))))
if D==0:
    print(int(((-1)*b)/(2*a)))