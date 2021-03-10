a=str(input())
if a=="11":
    print(str(a) + " " + "korov")
    exit()
if a=="1" or a[len(a)-1]=="1":
    print(str(a) + " " + "korova")
    exit()
if a=="12" or a=="13" or a=="14":
    print(str(a) + " " + "korov")
    exit()
if a[len(a)-1]=="2" or a[len(a)-1]=="3" or a[len(a)-1]=="4":
    print(str(a) + " " + "korovy")
    exit()
print(str(a) + " " + "korov")
