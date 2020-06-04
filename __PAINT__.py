from tkinter import *
from tkinter import colorchooser as ch
import sys

class PAINT:
     def __init__(self, master):
          self.master=master
          #self.master.attributes('-fullscreen', True)
          self.small="300x300"
          self.master.bind("<Q>", self.smallScreen)
          self.pcolor="black"
          #self.pc="black"
          self.state="cross"
          self.ox, self.oy=None, None
          self.store={"x":0,"y":0,"x2":0,"y2":0}
          self.pensize=2
          self.dw()

     def smallScreen(self, e):
          self.master.withdraw()
          sys.exit()
     def smallScreen2(self):
          #self.master.withdraw()
          #sys.exit()
          self.master.iconify()
     def dw(self):
          self.scr=Frame(self.master, height=900, width=900)
          self.scr.pack(side=TOP)

          self.scr.bind("<ButtonPress-1>", self.cord)
          
          self.tools=Frame(self.master,bg="gray", height=10, width=100)
          self.tools.place(x=0, y=0)
          
          self.c=Canvas(self.scr, height=500, width=900, cursor=self.state)
          self.c.pack()

          self.c['bg']="#fff"

          self.increment=Frame(self.scr)
          self.increment.pack(side=RIGHT)

          self.ps=Scale(self.increment, from_=2, to=100, orient=HORIZONTAL, command=self.change_ps)
          self.ps.pack()
          
          self.c.bind("<B1-Motion>", self.free)
          self.c.bind("<ButtonRelease-1>", self.reset)

          self.line=Button(self.tools, text="LINE",command=self.dL, cursor=self.state)
          self.line.pack()

          self.frH=Button(self.tools, text="FREE HAND", command=self.freeH, cursor=self.state)
          self.frH.pack()

          self.cALL=Button(self.tools, text="CLEAR CANVAS!", command=self.cC, cursor=self.state)
          self.cALL.pack()

          self.eraser=Button(self.tools, text="ERASER", command=self.eC, cursor=self.state)
          self.eraser.pack()

          self.pC=Button(self.increment, text="BRUSH COLOR!", command=self.change_b)
          self.pC.pack()

          self.c['cursor']=self.state 
          self.c.bind("<ButtonPress-1>", self.cord)

          self.tools=Frame(self.master,bg="gray", height=700, width=600)
          self.tools.place(relx=.0, rely=.20)

          self.rectTool=Button(self.tools, text="RECTANGLE", command=self.drawRECT)
          self.rectTool.pack()

          self.minimise=Button(self.master, text="____", command=self.smallScreen2)
          self.minimise.place(x=1300, y=10)

          self.circ=Button(self.master, text="CIRCLE", command=self.act_circle)
          self.circ.pack()

          self.poly=Button(self.master, text="TRIANGLE", command=self.POLY)
          self.poly.pack()

     def mini(self):
          self.master.geometry("500x300")

     def free(self, e):
          
          if self.ox and self.oy:
               self.c.create_line(self.ox, self.oy, e.x, e.y, width=self.pensize,fill=self.pcolor,capstyle=ROUND)
          self.ox, self.oy = e.x, e.y
     def reset(self, e):
          self.ox, self.oy=None, None

     def click(self, e):
          self.store["x"]=e.x
          self.store["y"]=e.y
          
          self.cr=self.c.create_line(e.x, e.y, e.x, e.y,fill=self.pcolor, width=self.pensize, capstyle=ROUND)

     def drag(self, e):
          self.store["x2"]=e.x
          self.store["y2"]=e.y

          self.c.coords(self.cr, self.store["x"],self.store["y"],
                        self.store["x2"],self.store["y2"])

     def dL(self):
          self.c.bind("<ButtonPress-1>",self.click)
          self.c.bind("<B1-Motion>",self.drag)
          self.state="cross"

     def freeH(self):
          self.c.bind("<B1-Motion>", self.free)
          self.c.bind("<ButtonRelease-1>", self.reset)
          self.state="cross"

     def cC(self):
          self.c.delete(ALL)

     def eC(self):
          self.pcolor="white"
          self.state="dotbox"
          self.c.bind("<B1-Motion>", self.free)
          self.c.bind("<ButtonRelease-1>", self.reset)

     def change_ps(self, e):
          self.pensize=e

     def change_b(self):
          self.pcolor=ch.askcolor()[1]

     def cord(self, e):
          print(e.x, e.y)

     def clickRect(self, e):
          self.rx, self.ry=e.x, e.y
          self.clR=self.c.create_rectangle(e.x, e.y, e.x, e.y, outline=self.pcolor, width=self.pensize)
          #print(self.rx, self.ry)
     def dragRect(self, e):
          self.rx2, self.ry2 = e.x, e.y
          self.c.coords(self.clR, self.rx, self.ry, self.rx2, self.ry2)
          #print(self.rx2, self.ry2)

     def drawRECT(self):
          self.c.bind("<ButtonPress-1>", self.clickRect)
          self.c.bind("<B1-Motion>", self.dragRect)

     def act_circle(self):
          self.c.bind("<ButtonPress-1>", self.clickC)
          self.c.bind("<B1-Motion>", self.dragC)

     def clickC(self, e):
          self.cx, self.cy=e.x, e.y
          self.cID=self.c.create_oval(e.x, e.y, e.x, e.y, outline=self.pcolor, width=self.pensize)

     def dragC(self, e):
          self.cx2, self.cy2 = e.x, e.y
          self.c.coords(self.cID, self.cx, self.cy, self.cx2, self.cy2)

     def cord(self, e):
          print(e.x ,e.y)

     def clickP(self, e):
          self.px,self.py=e.x, e.y
          self.pid=self.c.create_polygon(e.x, e.y, e.x, e.y, outline=self.pcolor, width=self.pensize)

     def dragP(self, e):
          self.px2, self.py2=e.x, e.y
          self.c.coords(self.pid,self.pid2, self.px, self.py, self.px2, self.py2, self.px3, self.py3)
     def dragP2(self, e):
          self.px3, self.py3=e.x, e.y
          self.pid2=self.c.create_polygon(e.x, e.y)

     def POLY(self):
          self.c.bind("<ButtonPress-1>",self.clickP)
          self.c.bind("<B1-Motion>",self.dragP)
          

if __name__=="__main__":
     root=Tk()
     root['bg']="gray"
     PAINT(root)
     root.mainloop()
