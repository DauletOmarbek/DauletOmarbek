a=int(input())
b=int(input())
if a>0:
    print((a*b)%109)
if a<0:
    print((109+(a*b))%109)