t=int(input())
hour=(t//3600)%24
minutes=(t-(t//3600)*3600)//60
seconds=t%60

if len(str(minutes))==1:
    minutes="0"+str(minutes)

if len(str(seconds))==1:
    seconds="0"+str(seconds)

print(str(hour) + ":" + str(minutes) + ":" + str(seconds))