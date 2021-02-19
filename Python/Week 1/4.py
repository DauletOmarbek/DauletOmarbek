def largestAltitude(gain):
    a=int(0)
    b=int(0)
    for x in range(len(gain)):
        a+=int(gain[x])
        if b<a:
            b=a


            
    return b



gain=input().split()
print(largestAltitude(gain))


