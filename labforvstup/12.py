# -*- coding: utf -8 -*-
import Tkinter
import random
import time
import math 

HEIGHT = 500
WIDTH = 800
window =  Tkinter.Tk()
window.title('Bubble Blaster')
c = Tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()

ship_id = c.create_polygon(5,5,5,25,30,15,fill='red')
ship_id2 = c.create_oval(0,0,30,30,outline='red')
SHIP_RADIUS = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id,MID_X,MID_Y)
c.move(ship_id2,MID_X,MID_Y)

SHIP_SPEED = 10
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id,0,-SHIP_SPEED)
        c.move(ship_id2,0,-SHIP_SPEED)
    elif event.keysym == 'Down':
        c.move(ship_id,0,SHIP_SPEED)
        c.move(ship_id2,0,SHIP_SPEED)
    elif event.keysym == 'Left':
        c.move(ship_id,-SHIP_SPEED,0)
        c.move(ship_id2,-SHIP_SPEED,0)
    elif event.keysym == 'Right':
        c.move(ship_id,SHIP_SPEED,0)
        c.move(ship_id2,SHIP_SPEED,0)
c.bind_all('<Key>',move_ship)

bubble_id = list()
bubble_radius = list()
bubble_speed = list()
MIN_BUBBLE_RADIUS = 10
MAX_BUBBLE_RADIUS = 30
MAX_BUBBLE_SPEED = 10
GAP = 100

def create_bubble():
    x = WIDTH + GAP
    y = random.randint(0, HEIGHT)
    r = random.randint(MIN_BUBBLE_RADIUS, MAX_BUBBLE_RADIUS)
    id1 = c.create_oval(x-r, y-r, x+r, y+r, outline='white')
    bubble_id.append(id1)
    bubble_radius.append(r)
    bubble_speed.append(random.randint(1,MAX_BUBBLE_SPEED))

def move_bubbles():
    for i in range(len(bubble_id)):
        c.move(bubble_id[i], -bubble_speed[i], 0)

def get_coords(id):
    pos = c.coords(id)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

def del_bubble(id):
    del bubble_radius[id]
    del bubble_speed[id]
    c.delete(bubble_id[id])
    del bubble_id[id]

def clean_up_bubbles():
    for id in range(len(bubble_id)-1,-1,-1):
        x,y = get_coords(bubble_id[id])
        if x < -GAP:
            del_bubble(id)

def distance(id1,id2):
    x1, y1 = get_coords(id1) 
    x2, y2 = get_coords(id2) 
    return math.sqrt((x2-x1)**2+(y2-y1)**2) 

# Функція, що перевіряє факт зіткнення
def collision():
    # Набрані очки (великі й швидкі бульбашки коштують дорожче)
    points = 0
    # Перебор усіх бульбашок (від останніх до перших, щоб уникнути помилок при видаленні бульбашок)
    for id in range(len(bubble_id)-1,-1,-1):
        d = distance(ship_id2, bubble_id[id]) # відстань між бульбашкою й човном
        b  = SHIP_RADIUS + bubble_radius[bubble] # сума радіусів бульбашки й човна
        if d < b: # Якщо відбулося зіткнення 
            points += bubble_radius[id] + bubble_speed[id] # нараховуємо очки
            del_bubble(id) # видаляємо бульбашку
    return points # повертаємо набрані очки

BUBBLE_CHANCE = 10
while True:
    if random.randint(1, BUBBLE_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    clean_up_bubbles()
    window.update()
    time.sleep(0.01)





