import string


str = input()
if len(str)%2==0:
    n = len(str) / 2
    for x in range(len(str)):
        
        if x < n-1:
            print(str[x],end="")
            print("(",end="")
        elif x+1 == n or x == n:
            print(str[x],end="")
        else:
            print(")",end="")
            print(str[x],end="")
else:
    n = len(str) // 2
    
    for x in range(len(str)):
        
        if x < n:
            print(str[x],end="")
            print("(",end="")
        elif x == n:
            print(str[x],end="")
        else:
            print(")",end="")
            print(str[x],end="")
    

    #(1(2(3)4)5)