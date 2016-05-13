# -*- coding: utf -8 -*-
import Tkinter
#модуль для генерації випадкових чисел
import random

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

# don't abbreviate, it's bad style and not 'pythonic'
SHIP_SPD = 10
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id,0,-SHIP_SPD)
        c.move(ship_id2,0,-SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship_id,0,SHIP_SPD)
        c.move(ship_id2,0,SHIP_SPD)
    elif event.keysym == 'Left':
        c.move(ship_id,-SHIP_SPD,0)
        c.move(ship_id2,-SHIP_SPD,0)
    elif event.keysym == 'Right':
        c.move(ship_id,SHIP_SPD,0)
        c.move(ship_id2,SHIP_SPD,0)
c.bind_all('<Key>',move_ship)

#Створюємо три пустих списки для збереження бульбашок
bubble_id = list() # список ідентифікаторів ("імен")
bubble_radius = list() # список радіусів
bubble_speed = list() # список швидкостей
MIN_BUBBLE_RADIUS = 10 # мінімальний радіус бульбашки
MAX_BUBBLE_RADIUS = 30 # максимальний радіус бульбашки
MAX_BUBBLE_SPEED = 10 # максимальна швидкість бульбашки
GAP = 100

# Функція створення нової бульбашки
def create_bubble():
    # позиція бульбашки на полотні
    x = WIDTH + GAP # координата x за правим краєм ігрового поля
    y = random.randint(0, HEIGHT) # координата y — випадкова
    # радіус бульбашки (випадковий від мінімального до максимального)
    r = random.randint(MIN_BUBBLE_RADIUS, MAX_BUBBLE_RADIUS)
    # створюємо новий об’єкт-еліпс на холсті
    id1 = c.create.oval(x-r, y-r, x+r, y+r, outline='white')
    # додаємо ім’я, радіус та швидкість бульбашки у відповідні списки
    bubble_id.append(id1)
    bubble_radius.append(r)
    bubble_speed.append(random.randint(1,MAX_BUBBLE_SPEED))

window.mainloop()
