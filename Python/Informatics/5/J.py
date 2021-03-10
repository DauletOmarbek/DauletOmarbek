a=str(input())
for x in range(len(a)):
    if a[x]!='.':
        print(a[x], end='')
    else:
        print(" ", end='')
