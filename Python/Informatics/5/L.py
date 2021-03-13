import math
a=float(input())
b=float(input())
c=float(input())
D=float(b*b-4*a*c)
if a==0 and b==0 and c==0:
    print(3)
    exit()
if D<0:
    print(0)
    exit()
if D>0:
    print(2, min(float(((-1)*b-math.sqrt(D))/(2*a)), float(((-1)*b+math.sqrt(D))/(2*a))), max(float(((-1)*b-math.sqrt(D))/(2*a)), float(((-1)*b+math.sqrt(D))/(2*a)))) 
if D==0:
    print(1, float(((-1)*b)/(2*a)))         