from datetime import date
data=[]

def ProcessInput(inputString):
    today = date.today()
    if(inputString=="film"):
        event=data[today][0]
    elif(inputString=="history"):
        event=data[today][1]
    elif(inputString=="music"):
        event=data[today][2]
    elif(inputString=="sport"):
        event=data[today][3]
    ret=today+event
    return ret
