import definitions
import pygame
import os
import sys
import time
import socket

header=64
port=6000
server='192.168.1.148'
addr=('', port)


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((server,port))

def send(message):
    msg=message.encode('utf-8')
    ml=len(msg)
    sl=str(ml).encode('utf-8')
    sl+=b' '*(header-len(sl))
    client.send(sl)
    client.send(msg)
    client.recv(header)

size_offsets=[
    (0,0,0),
    (1,0,0), #(id,xoffset,yoffset)
    (2,0,0),
    (3,0,0),
    (4,0,0),
    (5,0,0),
    (6,0,0),
    (7,0,0),
    (8,0,0),
    (9,0,0),
    (10,0,60),
    (11,0,60),
    (12,0,60),
    (13,0,60),
    (16,0,0),
    (18,60,0),
    (19,30,0),
    (20,0,0),
    (21,0,0),
    (29,0,0),
    (30,0,0),
    (35,0,0),
    (36,0,0),
    (39,0,0),
    (40,0,0),
    (41,0,30),
    (45,15,60),
    (46,15,60),
    (47,0,60),
    (67,0,0),
    (84,0,0),
    (99,0,60),
    (101,0,60),
    (111,0,60),
    (140,0,0),
    (141,0,0),
    (191,0,0),
    (200,0,25),
    (201,0,60),
    (202,15,60),
    (203,60,30),
    (286,0,60),
    (287,0,60),
]
pos_offsets=[
    (0,0,0),
    (1,0,0), #(id,xoffset,yoffset)
    (2,0,0),
    (3,0,0),
    (4,0,0),
    (5,0,0),
    (6,0,0),
    (7,0,0),
    (8,0,0),
    (9,0,0),
    (10,0,-30),
    (11,0,-30),
    (12,0,-30),
    (13,0,-30),
    (16,0,0),
    (18,30,0),
    (19,0,0),
    (20,0,0),
    (21,0,0),
    (29,0,0),
    (30,0,0),
    (35,0,0),
    (36,0,0),
    (39,0,0),
    (40,0,0),
    (41,0,-30),
    (45,0,-30),
    (46,0,-30),
    (47,0,-30),
    (67,0,0),
    (84,0,0),
    (99,0,-30),
    (101,0,-30),
    (111,0,-30),
    (140,0,0),
    (141,0,0),
    (191,0,0),
    (200,0,0),
    (201,0,-30),
    (202,-15,-30),
    (203,-30,-5),
    (286,0,-30),
    (287,0,-30),
]

class RenderText():
    def render(pos:tuple,text:str,surface:pygame.Surface,color:tuple,font:pygame.font.Font):
        surface.blit(font.render(text,True,color),pos)

if __name__=="main":
    pass

# imgs
wicon=pygame.image.load(definitions.wico)
bsize=30
# init
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_icon(wicon)
bg_color=(45,125,255)
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption("gdonline - colaborative level editor")
pygame.display.flip()
mpos=pygame.mouse.get_pos()
clock=pygame.time.Clock()

pusab=pygame.font.Font('font/pusab.otf',24)
pusab2=pygame.font.Font('font/pusab.otf',48)
helv=pygame.font.Font('font/helvetica.ttf',20)

objcount=0

mousedown=False
currentdraw=0
lastdraw=()
bid=1

leveldata=[]

class UIButton():
    def __init__(self, image, xpos, ypos, text_input, action) -> None:
        self.image=image
        self.xpos=xpos
        self.ypos=ypos
        self.rect=self.image.get_rect(center=(self.xpos,self.ypos))
        self.text_input=text_input
        self.text=pusab.render(self.text_input,True,(255,255,255))
        self.text_rect=self.text.get_rect()
        self.action=action
    
    def update(self):
        screen.blit(self.image,self.rect)
        screen.blit(self.text,self.text_rect)
    
    def checkForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,self.rect.bottom):
            exec(self.action)
            return True
        else:
            return False
tmb=pygame.image.load(definitions.triggerbg)
tmb=pygame.transform.scale(tmb,(1070/1.5,665/1.5))
tb=pygame.image.load(definitions.triggerblack)

class UITextInput():
    def __init__(self,bgimg,xpos,ypos,placeholder):
        self.bgimg=bgimg
        self.xpos=xpos
        self.ypos=ypos
        self.rect=bgimg.get_rect(center=(self.xpos,self.ypos))
        self.placeholdertext=placeholder
    def update(self):
        screen.blit(tb,(0,0))
        screen.blit(tmb,(1280/5,720/5))
        self.placeholder=RenderText.render((self.xpos,self.ypos),self.placeholdertext,screen,(255,255,255),pusab)
        

ok=pygame.image.load(definitions.ok)
ok=pygame.transform.scale(ok,(392/2.5,142/2.5))

class EditorMenu():
    def __init__(self, title) -> None:
        self.title=title
    def update(self):
        screen.blit(tb,(0,0))
        screen.blit(tmb,(1280/5,720/5))
        RenderText.render((1280/2-96,720/5+18),self.title,screen,(255,255,255),pusab2)
        RenderText.render((1280/3-10,720/5+65),"pulling a robtop and not finishing this menu",screen,(255,255,255),helv)
        okbtn=UIButton(ok,1280/2-40,540,"",f"close_{self.title}()")
        bms=pygame.mouse.get_pressed()
        if bms[0]==True:
            okbtn.checkForInput(pygame.mouse.get_pos())
        okbtn.update()
 
def ShowRotation():

    bui=pygame.image.load(definitions.empty)
    bui=pygame.transform.scale(bui,(60,60))
    screen.blit(bui,(1213, 90-12))
    global brot
    global bid
    exec(f"sw=pygame.image.load(definitions.id{bid});sw=pygame.transform.scale(sw,(35,35));sw=pygame.transform.rotate(sw,{brot});screen.blit(sw,(1225, 90))")

empty_ids=[]

def drawEditorGrid(blockSize, moffset:tuple):
    global currentdraw
    global gridpos
    global lastdraw
    currentdraw=0
    if blockSize <=0:
        blockSize=5
        global bsize
        bsize=5
    for x in range(0, 1280, blockSize):
        for y in range(0, 600, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, definitions.WHITE, rect, 1)
            dd=({currentdraw},{x},{y})
            lastdraw=dd
            currentdraw+=1

def loadBlock(id):
    global bid
    bid=id

def appedObjectDraw(what):
    global objcount
    global draws
    global leveldata
    global brot
    cmd=what.split(",")
    if float(cmd[3].replace(')',''))<600:  
        leveldata.append((float(cmd[1]),float(cmd[2]),float(cmd[3].replace(')','')), brot)) #(id,xpos,ypos, rot)
        draws.append(what)
        objcount+=1
        send(f"({float(cmd[1])}, {float(cmd[2])},{float(cmd[1])},{brot})")
draws=[]

def ZoomIn():
    global bsize
    bsize+=5

def ZoomOut():
    global bsize
    bsize-=5

def gen(save=False):
    s=time.time()
    global saving
    if save: saving=True
    f=open("data.txt","w")
    global leveldata
    first=True
    for data in leveldata:
        os.system("cls")
        xpos=round(data[1],2)
        ypos=round(data[2],2)
        rot=data[3]
        newdata=(data[0],xpos,ypos,rot)
        if first:
            f.write(f"{str(newdata)}")
            first=False
        else:
            f.write(f";{str(newdata)}")
    f.close()
    if save:
        saving=False
        return
    e=time.time()
    os.system(f"python {os.getcwd()}/levelgenerator.py")
    pygame.quit()
    sys.exit()


def DrawImage(image:str, id, xpos, ypos, rot=0):
    global bsize
    global bgti
    global obgm
    global brot
    
    img=pygame.image.load(image)
    for o in size_offsets:
        if o[0]==id:
            img=pygame.transform.scale(img,(bsize+o[1],bsize+o[2])) #(xsize,ysize)
            img=pygame.transform.rotate(img,rot)
    # snap xpos
    if xpos%bsize>15: xpos-=(xpos%bsize)-bsize
    else: xpos-=(xpos%bsize)
    if ypos%bsize>15: ypos-=(ypos%bsize)-bsize
    else: ypos-=(ypos%bsize)
    if ypos<600:
        screen.blit(img,(xpos,ypos))

tbg=pygame.image.load(definitions.triggerbg)
tbg=pygame.transform.scale(tbg,(1070/1.5, 665/1.5))

cfg=open('config.txt','r')
cfg=cfg.readlines()
ip=cfg[0].split(" ")

hm=EditorMenu('help')

saving=False

def stats():
    RenderText.render((0,2),str(f"FPS: {round(clock.get_fps(),2)}"),screen,(255,255,255),pusab)
    global currentdraw
    RenderText.render((0,28),str(f"rendered: {currentdraw}"),screen,(255,255,255),pusab)
    global lastdraw
    RenderText.render((0,54),f"last draw: {lastdraw[0]},{lastdraw[1]},{lastdraw[2]}",screen,(255,255,255),pusab)
    global objcount
    RenderText.render((0,54+26),f'objects: {objcount}',screen,(255,255,255),pusab)

brot=0

msg=pygame.image.load(definitions.message)
msg=pygame.transform.scale(msg,(1299/2,160/2))

def rotateLeft():
    print("rotateLeft")
    global brot
    brot-=90
    if brot==-360:
        brot=0

def rotateRight():
    print("rotateRight")
    global brot
    brot+=90
    if brot==360:
        brot=0

def loadLastSave():
    global brot
    global draws
    draws.clear()
    currentparse=1
    s=definitions.levelgenerator.loadLevel()
    print(s)
    s=s.split(";")
    for a in s:
        a=a.replace(")","")
        a=a.split("(")
        try:
            a.remove('')
        except:
            pass
        try:
            a=a[0]
            pass
        except:
            print("Possibly corrupted save file.")
            return
        a=a.split(",")
        id=a[0]
        x=a[1]
        y=a[2]
        rot=a[3]
        id=int(str(id).replace(".0",""))
        exec(f"DrawImage(definitions.id{id},{id},{x},{y},{rot})")
        appedObjectDraw(f'DrawImage(definitions.id{id},{id},{x},{y},{rot})')
        currentparse+=1
    loaded=True

def delete():
    global bsize
    global draws
    m=pygame.mouse.get_pos()
    x=m[0]
    y=m[1]
    del m
    if x%bsize>15: x-=(x%bsize)-bsize
    else: x-=(x%bsize)
    if y%bsize>15: y-=(y%bsize)-bsize
    else: y-=(y%bsize)
    for b in draws:
        i=draws.index(b)
        b=b.split("(")
        b=b[1].split(",")
        bx=float(b[2])
        by=b[3].replace(")","")
        by=float(by)

gb=pygame.image.load(definitions.generate)
gb=pygame.transform.scale(gb,(585/3.9,160/3.9))

hb=pygame.image.load(definitions.help)
hb=pygame.transform.scale(hb, (60,60))

ls=pygame.image.load(definitions.lls)
ls=pygame.transform.scale(ls,(585/3.9,160/3.9))

rl=pygame.image.load(definitions.rl)
rl=pygame.transform.scale(rl,(45,45))
rr=pygame.image.load(definitions.rr)
rr=pygame.transform.scale(rr,(45,45))

for i in range(1, 1916):
    empty_ids.append(i)
directory=os.getcwd()+'/ui/object selection/'
for file in os.listdir(directory):
    name=file.split(".")
    name=name[0]
    name=int(name)
    empty_ids.remove(name)

# buttons
oby=0
objx=0
x=0
row=0
for i in range(1,1916):
    if i not in empty_ids:
        if i in [36]:
            x=0
            oby+=50
        exec(f'b{i}=pygame.image.load(definitions.b{i});b{i}=pygame.transform.scale(b{i},(40,40));ob{i}=UIButton(b{i},{24+(50*x+objx)},{630+oby},"","loadBlock({i})")')
        x+=1

def reload():
    os.startfile('main.py')
    pygame.quit()

def help():
    global mopen
    mopen[0]=True

def showHelp():
    global mopen
    if mopen[0]==True:
        hm.update()

def close_help():
    global mopen
    mopen[0]=False

def processData(data):
    print(data)

running=True

# btns
generate=UIButton(gb,1150,635,"","gen()")
lls=UIButton(ls,1150,690,"","loadLastSave()")
rleft=UIButton(rl,1253,635,"","rotateLeft()")
rright=UIButton(rr,1253,690,"","rotateRight()")
hp=UIButton(hb,1240, 40, "", "help()")

# menu open
mopen=[False] # 0:help

while running:
    kstate=pygame.key.get_pressed()
    mstate=pygame.mouse.get_pressed()
    stop=False
    events=pygame.event.get()
    clock.tick(60)
    for event in events:
        if event.type==pygame.QUIT:
            running=False
            send("disc")
            pygame.quit()
            sys.exit()
    if kstate[pygame.K_DELETE] or kstate[pygame.K_BACKSPACE]:
        print("deleted")
        delete()
    if kstate[pygame.K_ESCAPE] and saving==False:
        pygame.quit()
        sys.exit()
    if kstate[pygame.K_s] and kstate[pygame.K_LCTRL]:
        print("saving...")
        gen(True)
        print("saved.")
    if kstate[pygame.K_r] and kstate[pygame.K_LCTRL]:
        reload()
    if kstate[pygame.K_q]:
        rotateLeft()
    if kstate[pygame.K_e]:
        rotateRight()
    if mstate[0]==True and mousedown==False:
        mousedown=True
        print("mouse down")
        pos=pygame.mouse.get_pos()
        gi=generate.checkForInput(pos)
        rleft.checkForInput(pos)
        rright.checkForInput(pos)
        lls.checkForInput(pos)
        for i in range(1,1916):
            if i not in empty_ids:
                exec(f'ob{i}.checkForInput({pos})')
        if hp.checkForInput(pos)==False:
            for p in pos_offsets:
                if p[0]==bid:
                    xpos=(pos[0]-25*bsize/45)+p[1]
                    ypos=(pos[1]-25*bsize/45)+p[2]
            appedObjectDraw(f'DrawImage(definitions.id{bid},{bid},{xpos},{ypos},{brot})')
    elif mstate[0]==False and mousedown==True:
        print("mouse up")
        mousedown=False
    # layering
    screen.fill(bg_color) # l0
    drawEditorGrid(bsize,pygame.mouse.get_pos()) #l1
    for d in draws:
        exec(d) # l2
    generate.update()
    lls.update()
    rright.update()
    rleft.update()
    hp.update()
    ShowRotation()
    for i in range(1,1916):
        if i not in empty_ids:
            exec(f'ob{i}.update()')
    showHelp()
    stats() # top layer
    pygame.display.update()