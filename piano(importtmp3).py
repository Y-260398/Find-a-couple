# -*- coding: utf-8 -*-
import pygame
from pygame import *
import random
import time

x=750
y=500

size=(x,y)

Fone=(255,140,200)
black=(0,0,0)
white=(255,255,255)


screen=pygame.display.set_mode(size)
pygame.display.set_caption('asbasb')

done=False
clock=pygame.time.Clock()
x=0


mx=[]
my=[]
pygame.mouse.get_pos(mx,my)
event.pos=(mx,my)

#карточка1
rx=(90)   #координаты левой верхней точки
ry=(50)   #по x и у
point1=(rx,ry)

wigth = 100   #ысота и ширина
height = 150
#kкарточка1


#карточка2
x2=(20)
y2=(250)
point2=(rx,ry)

wigth2 = 100
height2 = 150
#карточка2


#kartohka3
x3=(150)
y3=(20)
point3=(rx,ry)

wigth3 = 100
height3 = 150
#kartohka3



#kartohka4
x4=(150)
y4=(250)
point4=(rx,ry)

wigth4 = 100
height4 = 150
#kartohka4


#kartohka5
x5=(280)
y5=(20)
point5=(rx,ry)

wigth5 = 100
height5 = 150
#kartohka5

#kartohka6
x6=(280)
y6=(250)
point6=(rx,ry)

wigth6 = 100
height6 = 150
#kartohka6

#kartohka7
x7=(410)
y7=(20)
point7=(rx,ry)

wigth7 = 100
height7 = 150
#kartohka7

#kartohka8
x8=(410)
y8=(250)
point8=(rx,ry)

wigth8 = 100
height8 = 150
#kartohka8

#kartohka9
x9=(540)
y9=(20)
point9=(x,y)

wigth9 = 100
height9 = 150
#kartohka9

#kartohka10
x10=(540)
y10=(250)
point10=(x,y)

wigth10 = 100
height10 = 150
#kartohka10





screen=pygame.display.set_mode(size)
pygame.display.set_caption('Card Game v0.1 closed beta')
done=False
clock=pygame.time.Clock()
x=0

while not done:     #основной цикл программы
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True



            if (mx-rx<=wigth and mx-rx>=0) and (my-ry<=height and my-ry>=0):
                    pygame.mixer.load('collect.mp3')


        screen.fill(Fone)
        a=pygame.draw.rect(screen,black,[90,50,100,150],0)            #kvadrat1
        b=pygame.draw.rect(screen,white,[20,250,100,150],0)




    pygame.display.flip()     #obnova ekrana
    clock.tick(20)           #tipa fps
pygame.quit()