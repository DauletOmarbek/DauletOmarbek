a=int(input())
for x in range(100,1000):
    b=str(x)
    if a==int(b[0])+int(b[1])+int(b[2]):
        print(x)