# -*- coding: utf -8 -*-
import Tkinter
from Tkinter import *

root=Tk()
button1=Button(root,text='ok',width=25,height=5,bg='black',fg='red',font='arial 14')


HEIGHT = 500
WIDTH = 800
size=(HEIGHT,WIDTH)
window =  Tkinter.Tk()
window.title('Bubble Blaster')
class Test:
   def __init__(self, master):
        c = Tkinter.Canvas(window, width=WIDTH, height=HEIGHT)
        c.pack()
        gif1=PhotoImage(file='222.gif')
        Canvas.create_image(500,800,image=gif1,anchor=size)

        ship_id = c.create_polygon(5,5,5,25,30,15,fill='red')
        ship_id2 = c.create_oval(0,0,30,30,outline='red')
        SHIP_R = 15
        MID_X = WIDTH / 2
        MID_Y = HEIGHT / 2
        c.move(ship_id,MID_X,MID_Y)
        c.move(ship_id2,MID_X,MID_Y)

        #відстань, на яку переміститься човен за один крок (визначає швидкість)
        SHIP_SPD = 10
        def move_ship(event):
            if event.keysym == 'Up': #користувач нажав клавішу "стрілка вгору"
                c.move(ship_id,0,-SHIP_SPD)
                c.move(ship_id2,0,-SHIP_SPD)
            elif event.keysym == 'Down': #користувач нажав клавішу "стрілка вниз"
                c.move(ship_id,0,SHIP_SPD)
                c.move(ship_id2,0,SHIP_SPD)
            elif event.keysym == 'Left': #користувач нажав клавішу "стрілка вліво"
                c.move(ship_id,-SHIP_SPD,0)
                c.move(ship_id2,-SHIP_SPD,0)
            elif event.keysym == 'Right': #користувач нажав клавішу "стрілка вправо"
                c.move(ship_id,SHIP_SPD,0)
                c.move(ship_id2,SHIP_SPD,0)
        #При натисканні будь-якої клавіши буде виконано функцію move_ship
        c.bind_all('<Key>',move_ship)

window.mainloop()
