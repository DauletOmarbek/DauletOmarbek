def subtractProductAndSum(n):
    a=int(1)
    b=int(0)
    for x in range(len(n)):
        a*=int(n[x])
        b+=int(n[x])
    return a-b
    
    
n=str(input())
print(subtractProductAndSum(n))