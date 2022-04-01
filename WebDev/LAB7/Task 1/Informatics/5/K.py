import math
a=float(input())
b=float(input())
c=float(input())
D=float(b*b-4*a*c)
if D<0:
    exit()
if D>0:
    print(min(float(((-1)*b-math.sqrt(D))/(2*a)), float(((-1)*b+math.sqrt(D))/(2*a))), max(float(((-1)*b-math.sqrt(D))/(2*a)), float(((-1)*b+math.sqrt(D))/(2*a)))) 
if D==0:
    print(float(((-1)*b)/(2*a)))        