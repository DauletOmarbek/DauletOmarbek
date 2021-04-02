n=int(input())
m=int(input())
a=int(input())
if n%a!=0:
    n=n//a+1
else:
    n=n//a
if m%a!=0:
    m=m//a+1
else:
    m=m//a+1
print(int(n*m))

