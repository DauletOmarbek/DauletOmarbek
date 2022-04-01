import math
a=int(input())
b=int(input())
c=int(input())
if a+b<=c or a+c<=b or b+c<=a:
    print("impossible")
    exit()
if math.sqrt(a*a+b*b)==c or math.sqrt(a*a+c*c)==b or math.sqrt(c*c+b*b)==a:
    print("rectangular")
    exit()
if c*c>a*a+b*b or a*a>b*b+c*c or b*b>a*a+c*c:
    print("obtuse")
    exit()
if c*c<a*a+b*b or a*a<b*b+c*c or b*b<a*a+c*c:
    print("acute")