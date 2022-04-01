a=int(input())
b=int(input())
if (b%a==0):
    print(0)
if (b%a>0):
    print(a-b%a)