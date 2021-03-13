
b=dict()

for x in range(5):
    a=str(input())

    first, second =a.split()
    if first in b:
        b[first]+=int(second)
    else:
        b[first]=int(second)
for x in b:
    print(x, b[x])