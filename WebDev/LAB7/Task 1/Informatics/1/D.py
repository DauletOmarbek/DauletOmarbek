a=0
for x in range(1,11):
    if x%2==1:
        a+=4/(2*x-1)
    else:
        a-=4/(2*x-1)
print(a)