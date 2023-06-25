f=open("data.txt","r")
import base64
import string
import random

def gdoEncode(e):
    pass

def gdoDecode(e):
    pass

def saveLevel():
    global f
    data=f.read()
    data=data.encode('ascii')
    data=base64.b85encode(data)
    data=data.decode('ascii')
    f=open('data.txt','w')
    f.write(data)
    print("level saved")

def loadLevel() -> str:
    global f
    data=f.read()
    data=data.encode('ascii')
    data=base64.b85decode(data)
    data=data.decode('ascii')
    print("level data decoded.")
    return data

if __name__=="__main__":
    saveLevel()