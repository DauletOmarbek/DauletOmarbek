a=int(input())
b=int(input())
for x in range(a,b+1):
    c=str(x)
    for y in range(0,11):
        d=int(0)
        if int(c[0])==y:
            d+=1
        if int(c[1])==y:
            d+=1
        if int(c[2])==y:
            d+=1
        if int(c[3])==y:
            d+=1
        if d==3:
            print(x)