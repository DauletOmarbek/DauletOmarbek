import math
a=int(input())
if a==1:
    print("False")
    exit()
for x in range(2,a):
    if a%(x)==0:
        print("False")
        exit()
print('True')