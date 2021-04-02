a=int(input())
f=int(0)
for x in range(1,a+1):
    if x%2==1:
        f-=x #f=f-x
    else:
        f+=x
print(f)

1/2+1/4+1/8