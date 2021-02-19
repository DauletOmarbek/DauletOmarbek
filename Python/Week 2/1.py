def foo(address):
    a=str()
    for x in range(len(address)-1):
        if address[x]==".":
            a+="[.]"
        else:
            a+=address[x]
    return a


address=input(str())
print(foo(address))