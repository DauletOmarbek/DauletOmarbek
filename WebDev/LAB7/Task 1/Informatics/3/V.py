a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if (d*e>=a*b and ((d>=a or d>=b) and (e>=a or e>=b))) or (d*e>=c*b and ((d>=c or d>=b) and (e>=c or e>=b))) or (d*e>=a*c and ((d>=a or d>=c) and (e>=a or e>=c))):
    print("YES")
else:
    print("NO")