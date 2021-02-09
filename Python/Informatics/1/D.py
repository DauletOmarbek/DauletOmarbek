a=0
for x in range(1,11):
    if x%2==1:
        a+=4/(2*x-1)
    if x%2==0:
        a-=4/(2*x-1)
print(a)