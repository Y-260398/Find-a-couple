# -*- coding: utf-8 -*-
from pygame.locals import*
import pygame
from pygame import *
import random
import time
import sys

x=750
y=500


size=(x,y)
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,255)
ColorDK=(255,50,120)
HZ=(200,250,190)
KZ=(250,250,60)
GB=(0,255,240)
RG=(255,240,0)
RB=(255,0,240)




screen=pygame.display.set_mode(size)
pygame.display.set_caption('Space Cards')


done=False
clock=pygame.time.Clock()
x=0


mx=[]
my=[]
pygame.mouse.get_pos(mx,my)
event.pos=(mx,my)
#карточка1
rx=(20)   #координаты левой верхней точки
ry=(20)   #по x и у
point1=(rx,ry)

wigth = 100   #ысота и ширина
height = 150
#kкарточка1
color1n = pygame.Surface([wigth, height])
color1n.fill(black)
black = color1n
red=pygame.transform.scale(pygame.image.load("150.jpg").convert(),[wigth, height]) #pygame.image.load("150.jpg").convert()



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
ColorDK=pygame.transform.scale(pygame.image.load("planeta.jpg").convert(),[wigth3, height3])

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



GB=pygame.transform.scale(pygame.image.load("space.jpg").convert(),[wigth5, height5])
RG=pygame.transform.scale(pygame.image.load("pro.jpg").convert(),[wigth9, height9])
blue=pygame.transform.scale(pygame.image.load("fentezi.jpg").convert(),[wigth7, height7])
Fone1 = pygame.image.load ("Solar.jpg").convert_alpha()

def draw_card(position,size,color1,color2,color3):
   pygame.draw.circle(screen,color1,color2,position,size)                   #это всё не надо...   оно тут просто так))) наверно...
for event in pygame.event.get():
   if event.type==pygame.quit:
      done=True

color1=black                #цвет карточек в тот момент когда они перевёрнуты...   мы не видем какой там цвет
color2=black
color3=black
color4=black
color5=black
color6=black
color7=black
color8=black
color9=black
color10=black
C=(color1 and color2 and color3 and color4 and color5 and color6 and color7 and color8 and color9 and color10)



while not done:     #основной цикл программы
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
        if event.type==pygame.MOUSEBUTTONDOWN:          #говорим что будем использовать мышку
                if event.button==1:    #говорим чтоб он реагировал только на левую кнопку мыши... "1"-левая кнопка мышки
                    pos = pygame.mouse.get_pos()
                    mx = pos[0]                     #x мышки
                    my = pos[1]                     #y мышки



                    if (mx-rx<=wigth and mx-rx>=0) and (my-ry<=height and my-ry>=0):    #вычисление координат квадрата... если там клацнуть то...
                            color1=red    #...то цвет поменяется с чёрного на красный
                    if (mx-x2<=wigth2 and mx-x2>=0) and (my-y2<=height2 and my-y2>=0):
                            color2=red
                    if (mx-x3<=wigth3 and mx-x3>=0) and (my-y3<=height3 and my-y3>=0):
                            color3=ColorDK
                    if (mx-x4<=wigth4 and mx-x4>=0) and (my-y4<=height4 and my-y4>=0):
                            color4=blue
                    if (mx-x5<=wigth5 and mx-x5>=0) and (my-y5<=height5 and my-y5>=0):
                            color5=blue
                    if (mx-x6<=wigth6 and mx-x6>=0) and (my-y6<=height6 and my-y6>=0):
                            color6=ColorDK
                    if (mx-x7<=wigth7 and mx-x7>=0) and (my-y7<=height7 and my-y7>=0):
                            color7=GB
                    if (mx-x8<=wigth8 and mx-x8>=0) and (my-y8<=height8 and my-y8>=0):
                            color8=GB
                    if (mx-x9<=wigth9 and mx-x9>=0) and (my-y9<=height9 and my-y9>=0):
                            color9=RG
                    if (mx-x10<=wigth10 and mx-x10>=0) and (my-y10<=height10 and my-y10>=0):
                            color10=RG




    screen.fill(white)           #описание каждого квадрата... цвет, размер и тп...
    screen.blit(Fone1,[0,0])
    if color1 != Fone1:
        a=screen.blit(color1,(20,20))
    if color2 != Fone1:
        b=screen.blit(color2,(20,250))
    if color3 != Fone1:
        c=screen.blit(color3,(150,20))
    if color4 != Fone1:
        d=screen.blit(color4,(150,250))
    if color5 != Fone1:
        e=screen.blit(color5,(280,20))
    if color6 != Fone1:
        z=screen.blit(color6,(280,250))
    if color7 != Fone1:
        q=screen.blit(color7,(410,20))
    if color8 != Fone1:
        h=screen.blit(color8,(410,250))
    if color9 != Fone1:
        p=screen.blit(color9,(540,20))
    if color10 != Fone1:
        o=screen.blit(color10,(540,250))



    if color1==red and color2==red:
            color1=Fone1
            color2=Fone1
    if color3==ColorDK and color6==ColorDK:
           color3=Fone1
           color6=Fone1
    if color4==blue and color5==blue:
           color4=Fone1
           color5=Fone1
    if color7==GB and color8==GB:
           color7=Fone1
           color8=Fone1
    if color9==RG and color10==RG:
           color9=Fone1
           color10=Fone1
##

    if color1==red and color3==ColorDK:     #это что будет при том если мы выбираем карточки сс разными цветами...
            color1=black                        #они опять переворачиваются...  становятся чёрные
            color3=black
    if color1==red and color4==blue:
            color1=black
            color4=black
    if color1==red and color5==blue:
            color1=black
            color5=black
    if color1==red and color6==ColorDK:
            color1=black
            color6=black
    if color1==red and color7==GB:
            color1=black
            color7=black
    if color1==red and color8==GB:
            color1=black
            color8=black
##
    if color2==red and color3==ColorDK:
            color2=black
            color3=black
    if color2==red and color4==blue:
            color2=black
            color4=black
    if color2==red and color5==blue:
            color2=black
            color5=black
    if color2==red and color6==ColorDK:
            color2=black
            color6=black
    if color2==red and color7==GB:
            color2=black
            color7=black
    if color2==red and color8==GB:
            color2=black
            color8=black
    if color2==red and color9==RG:
            color2=black
            color9=black
    if color2==red and color10==RG:
            color2=black
            color10=black
##
    if color3==ColorDK and color2==red:
            color2=black
            color3=black
    if color3==ColorDK and color4==blue:
            color3=black
            color4=black
    if color3==ColorDK and color5==blue:
            color3=black
            color5=black
    if color3==ColorDK and color1==red:
            color3=black
            color6=black
    if color3==ColorDK and color7==GB:
            color3=black
            color7=black
    if color3==ColorDK and color8==GB:
            color3=black
            color8=black
    if color3==ColorDK and color9==RG:
            color2=black
            color9=black
    if color3==ColorDK and color10==RG:
            color3=black
            color10=black
##
    if color4==blue and color3==ColorDK:
            color4=black
            color3=black
    if color4==blue and color6==ColorDK:
            color4=black
            color6=black
    if color4==blue and color1==red:
            color1=black
            color4=black
    if color4==blue and color2==red:
            color4=black
            color2=black
    if color4==blue and color7==GB:
            color4=black
            color7=black
    if color4==blue and color8==GB:
            color4=black
            color8=black
    if color4==blue and color9==RG:
            color4=black
            color9=black
    if color4==blue and color10==RG:
            color4=black
            color10=black
##
    if color5==blue and color3==ColorDK:
            color5=black
            color3=black
    if color5==blue and color1==red:
            color1=black
            color5=black
    if color5==blue and color2==red:
            color2=black
            color5=black
    if color5==blue and color6==ColorDK:
            color5=black
            color6=black
    if color5==blue and color7==GB:
            color5=black
            color7=black
    if color5==blue and color8==GB:
            color5=black
            color8=black
    if color5==blue and color9==RG:
            color5=black
            color9=black
    if color5==blue and color10==RG:
            color5=black
            color10=black
##
    if color7==GB and color3==ColorDK:
            color7=black
            color3=black
    if color7==GB and color1==red:
            color1=black
            color7=black
    if color7==GB and color2==red:
            color2=black
            color7=black
    if color7==GB and color6==ColorDK:
            color7=black
            color6=black
    if color7==GB and color5==blue:
            color5=black
            color7=black
    if color7==GB and color4==blue:
            color4=black
            color7=black
    if color7==GB and color9==RG:
            color7=black
            color9=black
    if color7==GB and color10==RG:
            color7=black
            color10=black
##
    if color8==GB and color3==ColorDK:
            color8=black
            color3=black
    if color8==GB and color1==red:
            color1=black
            color8=black
    if color8==GB and color2==red:
            color2=black
            color8=black
    if color8==GB and color6==ColorDK:
            color8=black
            color6=black
    if color8==GB and color5==blue:
            color5=black
            color8=black
    if color8==GB and color4==blue:
            color4=black
            color8=black
    if color8==GB and color9==RG:
            color8=black
            color9=black
    if color8==GB and color10==RG:
            color8=black
            color10=black
##
    if color9==RG and color3==ColorDK:
            color9=black
            color3=black
    if color9==RG and color1==red:
            color1=black
            color9=black
    if color9==RG and color2==red:
            color2=black
            color9=black
    if color9==RG and color6==ColorDK:
            color9=black
            color6=black
    if color9==RG and color5==blue:
            color5=black
            color9=black
    if color9==RG and color4==blue:
            color4=black
            color9=black
    if color9==RG and color7==GB:
            color7=black
            color9=black
    if color9==RG and color8==GB:
            color8=black
            color9=black
##
    if color10==RG and color3==ColorDK:
            color10=black
            color3=black
    if color10==RG and color1==red:
            color1=black
            color10=black
    if color10==RG and color2==red:
            color2=black
            color10=black
    if color10==RG and color6==ColorDK:
            color10=black
            color6=black
    if color10==RG and color5==blue:
            color5=black
            color10=black
    if color10==RG and color4==blue:
            color4=black
            color10=black
    if color10==RG and color7==GB:
            color7=black
            color10=black
    if color10==RG and color8==GB:
            color8=black
            color10=black


    pygame.display.flip()     #obnova ekrana
    clock.tick(15)           #это fps
pygame.quit()        #konec