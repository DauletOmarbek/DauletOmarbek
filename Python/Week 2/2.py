def interpret(command):
    a=str()
    for x in range(len(command)):
        if command[x]=="(" and command[x+1]==")":
            a+="o"
            x=x+1
        elif (ord(command[x])>=97 and ord(command[x])<=122) or (ord(command[x])>=65 and ord(command[x])<=90):
            a+=command[x]
    return a

command = str(input())
print(interpret(command))