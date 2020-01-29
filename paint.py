from turtle import *
import random
Screen()
speed(0)
shape('circle')
shapesize(2)
pensize(3)
color('black')
down()
def m():
     up()
def draw():
     down()

def drag():
          ondrag(goto)
colors=['red','orange','green','black','brown','cyan']

def sw():
     color(random.choice(colors))
def cl():
     clear()
def s1():
     pensize(4)
def s2():
     pensize(5)
def eraser():
     shape('square')
     color('white','black')
     pensize(18)

bg=['red','yellow','green','crimson','white']

def ch_bg():
     bgcolor(random.choice(bg))
def back():
          shape('circle')
          shapesize(2)
          pensize(3)
          color('black')

listen()
onkeypress(m,'u')
drag()
onkeypress(sw,'c')
onkey(ch_bg,'space')
onkeypress(back,'P')
onkeypress(eraser,'E')
onkeypress(cl,'Escape')
onkey(s1,'1')
onkey(s2,'2')
onkeypress(draw,'d')
mainloop()
