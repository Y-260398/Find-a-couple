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



HZ=(200,250,190)
KZ=(250,250,60)


RB=(255,0,240)




screen=pygame.display.set_mode(size)
pygame.display.set_caption('Card Game v0.1 closed beta')
done=False
clock=pygame.time.Clock()
x=0


mx=[]
my=[]
pygame.mouse.get_pos(mx,my)
event.pos=(mx,my)

#kartohka1
rx=(20)
ry=(20)
point1=(rx,ry)

wigth = 100
height = 150
#kartohka1

red=pygame.transform.scale(pygame.image.load("150.jpg").convert(),[wigth, height]) #pygame.image.load("150.jpg").convert()

#kartohka2
x2=(20)
y2=(250)
point2=(rx,ry)

wigth2 = 100
height2 = 150
#kartohka2


#kartohka3
x3=(150)
y3=(20)
point3=(rx,ry)

wigth3 = 100
height3 = 150
#kartohka3

ColorDK=pygame.transform.scale(pygame.image.load("planeta.jpg").convert(),[wigth3, height3])

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

GB=pygame.transform.scale(pygame.image.load("space.jpg").convert(),[wigth5, height5])

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

blue=pygame.transform.scale(pygame.image.load("fentezi.jpg").convert(),[wigth7, height7])

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

RG=pygame.transform.scale(pygame.image.load("pro.jpg").convert(),[wigth9, height9])

#kartohka10
x10=(540)
y10=(250)
point10=(x,y)

wigth10 = 100
height10 = 150
#kartohka10

Fone1 = pygame.image.load ("Solar.jpg").convert_alpha()


def draw_card(position,size,color1,color2,color3):
    pygame.draw.circle(screen,color1,color2,position,size)
for event in pygame.event.get():
    if event.type==pygame.quit:
        done=True


color1=black
color2=black
color3=black
color4=black
color5=black
color6=black
color7=black
color8=black
color9=black
color10=black

A=[red,blue,ColorDK,RG,GB]
random.shuffle(A)
Q=[color1,color2,color3,color4,color5,color6,color7,color8,color9,color10]



while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
        if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    pos = pygame.mouse.get_pos()
                    mx = pos[0]                     #x mihki
                    my = pos[1]                     #y mihki


                    if (mx-rx<=wigth and mx-rx>=0) and (my-ry<=height and my-ry>=0):    #vichislenie tochek kvadrata
                            color1=A[1]
                    if (mx-x2<=wigth2 and mx-x2>=0) and (my-y2<=height2 and my-y2>=0):
                            color2=A[1]
                    if (mx-x3<=wigth3 and mx-x3>=0) and (my-y3<=height3 and my-y3>=0):
                            color3=A[2]
                    if (mx-x4<=wigth4 and mx-x4>=0) and (my-y4<=height4 and my-y4>=0):
                            color4=A[2]
                    if (mx-x5<=wigth5 and mx-x5>=0) and (my-y5<=height5 and my-y5>=0):
                            color5=A[4]
                    if (mx-x6<=wigth6 and mx-x6>=0) and (my-y6<=height6 and my-y6>=0):
                            color6=A[4]
                    if (mx-x7<=wigth7 and mx-x7>=0) and (my-y7<=height7 and my-y7>=0):
                            color7=A[6]
                    if (mx-x8<=wigth8 and mx-x8>=0) and (my-y8<=height8 and my-y8>=0):
                            color8=A[6]
                    if (mx-x9<=wigth9 and mx-x9>=0) and (my-y9<=height9 and my-y9>=0):
                            color9=A[8]
                    if (mx-x10<=wigth10 and mx-x10>=0) and (my-y10<=height10 and my-y10>=0):
                            color10=A[8]

    screen.fill(white)
    screen.blit(Fone1,(0,0))
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




    if color1==A[0]==color2==A[1]:
           color1=Fone
           color2=Fone
    if color1==A[0]==color3==A[2]:     #nead timeng
            color1=Fone
            color3=Fone
    if color1==A[0]==color4==A[3]:
            color1=Fone
            color4=Fone
    if color1==A[0] == color5==A[4]:
            color1=Fone
            color5=Fone
    if color1==A[0] == color6==A[5]:
            color1=Fone
            color6=Fone
    if color1==A[0] == color7==A[6]:
            color1=Fone
            color7=Fone
    if color1==A[0] == color8==A[7]:
            color1=Fone
            color8=Fone
    if color1==A[0] == color9==A[8]:
            color1=Fone
            color9=Fone
    if color1==A[0] == color10==A[9]:
            color1=Fone
            color10=Fone
##
    if color2==A[1] == color3==A[2]:     #nead timeng
            color2=Fone
            color3=Fone
    if color2==A[1] == color4==A[3]:
            color2=Fone
            color4=Fone
    if color2==A[1] == color5==A[4]:
            color2=Fone
            color5=Fone
    if color2==A[1] == color1==A[0]:
            color1=Fone
            color4=Fone
    if color2==A[1] == color6==A[5]:
            color2=Fone
            color6=Fone
    if color2==A[1] == color7==A[6]:
            color2=Fone
            color7=Fone
    if color2==A[1] == color8==A[7]:
            color2=Fone
            color8=Fone
    if color2==A[1] == color9==A[8]:
            color2=Fone
            color9=Fone
    if color2==A[1] == color10==A[9]:
            color2=Fone
            color10=Fone
##
    if color3==A[2]==color4==A[3]:
           color3=Fone
           color4=Fone
    if color3==A[2] == color2==A[1]:     #nead timeng
            color2=Fone
            color3=Fone
    if color3==A[2] == color5==A[4]:
            color3=Fone
            color5=Fone
    if color3==A[2] == color6==A[5]:
            color3=Fone
            color6=Fone
    if color3==A[2] == color1==A[0]:
            color3=Fone
            color6=Fone
    if color3==A[2] == color7==A[6]:
            color3=Fone
            color7=Fone
    if color3==A[2] == color8==A[7]:
            color3=Fone
            color8=Fone
    if color3==A[2] == color9==A[8]:
            color3=Fone
            color9=Fone
    if color3==A[2] == color10==A[9]:
            color3=Fone
            color10=Fone

##
    if color4==A[3] == color3==A[2]:     #nead timeng
            color4=Fone
            color3=Fone
    if color4==A[3] == color6==A[5]:
            color4=Fone
            color6=Fone
    if color4==A[3] == color1==A[0]:
            color1=Fone
            color4=Fone
    if color4==A[3] == color2==A[1]:
            color4=Fone
            color2=Fone
    if color4==A[3] == color7==A[6]:
            color4=Fone
            color7=Fone
    if color4==A[3] == color8==A[7]:
            color4=Fone
            color8=Fone
    if color4==A[3] == color9==A[8]:
            color4=Fone
            color9=Fone
    if color4==A[3] == color10==A[9]:
            color4=Fone
            color10=Fone
    if color4==A[3] == color5==A[4]:
            color4=Fone
            color5=Fone
##
    if color5==A[4]==color6==A[5]:
           color5=Fone
           color6=Fone
    if color5==A[4] == color3==A[2]:     #nead timeng
            color5=Fone
            color3=Fone
    if color5==A[4] == color4==A[3]:     #nead timeng
            color5=Fone
            color4=Fone
    if color5==A[4] == color1==A[0]:
            color1=Fone
            color5=Fone
    if color5==A[4] == color2==A[1]:
            color2=Fone
            color5=Fone
    if color5==A[4] == color7==A[6]:
            color5=Fone
            color7=Fone
    if color5==A[4] == color8==A[7]:
            color5=Fone
            color8=Fone
    if color5==A[4] == color9==A[8]:
            color5=Fone
            color9=Fone
    if color5==A[4] == color10==A[9]:
            color5=Fone
            color10=Fone
##
    if color7==A[6]==color8==A[7]:           #destroyed
            color7=Fone
            color8=Fone
    if color7==A[6] == color3==A[2]:     #nead timeng
            color7=Fone
            color3=Fone
    if color7==A[6] == color1==A[0]:
            color1=Fone
            color7=Fone
    if color7==A[6] == color2==A[1]:
            color2=Fone
            color7=Fone
    if color7==A[6] == color6==A[5]:
            color7=Fone
            color6=Fone
    if color7==A[6] == color5==A[4]:
            color5=Fone
            color7=Fone
    if color7==A[6] == color4==A[3]:
            color4=Fone
            color7=Fone
    if color7==A[6] == color9==A[8]:
            color7=Fone
            color9=Fone
    if color7==A[6] == color10==A[9]:
            color7=Fone
            color10=Fone
##
    if color6==A[5] == color3==A[2]:     #nead timeng
            color6=Fone
            color3=Fone
    if color6==A[5] == color1==A[0]:
            color1=Fone
            color6=Fone
    if color6==A[5] == color2==A[1]:
            color2=Fone
            color6=Fone
    if color6==A[5] == color8==A[7]:
            color6=Fone
            color8=Fone
    if color6==A[5] == color5==A[4]:
            color5=Fone
            color6=Fone
    if color6==A[5] == color4==A[3]:
            color4=Fone
            color6=Fone
    if color6==A[5] == color9==A[8]:
            color6=Fone
            color9=Fone
    if color6==A[5] == color10==A[9]:
            color6=Fone
            color10=Fone
    if color6==A[5] == color7==A[6]:
            color6=Fone
            color7=Fone
##
    if color8==A[7] == color3==A[2]:     #nead timeng
            color8=Fone
            color3=Fone
    if color8==A[7] == color1==A[0]:
            color1=Fone
            color8=Fone
    if color8==A[7] == color2==A[1]:
            color2=Fone
            color8=Fone
    if color8==A[7] == color6==A[5]:
            color8=Fone
            color6=Fone
    if color8==A[7] == color5==A[4]:
            color5=Fone
            color8=Fone
    if color8==A[7] == color4==A[3]:
            color4=Fone
            color8=Fone
    if color8==A[7] == color9==A[8]:
            color8=Fone
            color9=Fone
    if color8==A[7] == color10==A[9]:
            color8=Fone
            color10=Fone
    if color8==A[7] == color7==A[6]:
            color8=Fone
            color7=Fone
##
    if color9==A[8] == color3==A[2]:     #nead timeng
            color9=Fone
            color3=Fone
    if color9==A[8] == color1==A[0]:
            color1=Fone
            color9=Fone
    if color9==A[8] == color2==A[1]:
            color2=Fone
            color9=Fone
    if color9==A[8] == color6==A[5]:
            color9=Fone
            color6=Fone
    if color9==A[8] == color5==A[4]:
            color5=Fone
            color9=Fone
    if color9==A[8] == color4==A[3]:
            color4=Fone
            color9=Fone
    if color9==A[8] == color7==A[6]:
            color7=Fone
            color9=Fone
    if color9==A[8] == color8==A[7]:
            color8=Fone
            color9=Fone
    if color9==A[8] == color10==A[9]:
            color10=Fone
            color9=Fone
##
    if color10==A[9] == color3==A[2]:
            color10=Fone
            color3=Fone
    if color10==A[9] == color1==A[0]:
            color1=Fone
            color10=Fone
    if color10==A[9] == color2==A[1]:
            color2=Fone
            color10=Fone
    if color10==A[9] == color6==A[5]:
            color10=Fone
            color6=Fone
    if color10==A[9] == color5==A[4]:
            color5=Fone
            color10=Fone
    if color10==A[9] == color4==A[3]:
            color4=Fone
            color10=Fone
    if color10==A[9] == color7==A[6]:
            color7=Fone
            color10=Fone
    if color10==A[9] == color8==A[7]:
            color8=Fone
            color10=Fone
    if color10==A[9] == color9==A[8]:
            color8=Fone
            color10=Fone

############
    if color1==A[0] and color2==A[1]:     #nead timeng
            color1=black
            color2=black
    if color1==A[0] and color3==A[2]:     #nead timeng
            color1=black
            color3=black
    if color1==A[0] and color4==A[3]:
            color1=black
            color4=black
    if color1==A[0] and color5==A[4]:
            color1=black
            color5=black
    if color1==A[0] and color6==A[5]:
            color1=black
            color6=black
    if color1==A[0] and color7==A[6]:
            color1=black
            color7=black
    if color1==A[0] and color8==A[7]:
            color1=black
            color8=black
    if color1==A[0] and color9==A[8]:
            color1=black
            color9=black
    if color1==A[0] and color10==A[9]:
            color1=black
            color10=black
##
    if color2==A[1] and color3==A[2]:     #nead timeng
            color2=black
            color3=black
    if color2==A[1] and color1==A[0]:     #nead timeng
            color2=black
            color1=black
    if color2==A[1] and color4==A[3]:
            color2=black
            color4=black
    if color2==A[1] and color5==A[4]:
            color2=black
            color5=black
    if color2==A[1] and color6==A[5]:
            color2=black
            color6=black
    if color2==A[1] and color7==A[6]:
            color2=black
            color7=black
    if color2==A[1] and color8==A[7]:
            color2=black
            color8=black
    if color2==A[1] and color9==A[8]:
            color2=black
            color9=black
    if color2==A[1] and color10==A[9]:
            color2=black
            color10=black
##
    if color3==A[2] and color2==A[1]:     #nead timeng
            color2=black
            color3=black
    if color3==A[2] and color4==A[3]:
            color3=black
            color4=black
    if color3==A[2] and color5==A[4]:
            color3=black
            color5=black
    if color3==A[2] and color1==A[0]:
            color3=black
            color6=black
    if color3==A[2] and color7==A[6]:
            color3=black
            color7=black
    if color3==A[2] and color8==A[7]:
            color3=black
            color8=black
    if color3==A[2] and color9==A[8]:
            color3=black
            color9=black
    if color3==A[2] and color10==A[9]:
            color3=black
            color10=black
    if color3==A[2] and color6==A[5]:
            color3=black
            color6=black
##
    if color4==A[3] and color3==A[2]:     #nead timeng
            color4=black
            color3=black
    if color4==A[3] and color6==A[5]:
            color4=black
            color6=black
    if color4==A[3] and color1==A[0]:
            color1=black
            color4=black
    if color4==A[3] and color2==A[1]:
            color4=black
            color2=black
    if color4==A[3] and color7==A[6]:
            color4=black
            color7=black
    if color4==A[3] and color8==A[7]:
            color4=black
            color8=black
    if color4==A[3] and color9==A[8]:
            color4=black
            color9=black
    if color4==A[3] and color10==A[9]:
            color4=black
            color10=black
    if color4==A[3] and color5==A[4]:
            color4=black
            color5=black
##
    if color5==A[4] and color3==A[2]:     #nead timeng
            color5=black
            color3=black
    if color5==A[4] and color1==A[0]:
            color1=black
            color5=black
    if color5==A[4] and color2==A[1]:
            color2=black
            color5=black
    if color5==A[4] and color6==A[5]:
            color5=black
            color6=black
    if color5==A[4] and color7==A[6]:
            color5=black
            color7=black
    if color5==A[4] and color8==A[7]:
            color5=black
            color8=black
    if color5==A[4] and color9==A[8]:
            color5=black
            color9=black
    if color5==A[4] and color10==A[9]:
            color5=black
            color10=black
    if color5==A[4] and color4==A[3]:
            color5=black
            color4=black
##
    if color7==A[6] and color3==A[2]:     #nead timeng
            color7=black
            color3=black
    if color7==A[6] and color1==A[0]:
            color1=black
            color7=black
    if color7==A[6] and color2==A[1]:
            color2=black
            color7=black
    if color7==A[6] and color6==A[5]:
            color7=black
            color6=black
    if color7==A[6] and color5==A[4]:
            color5=black
            color7=black
    if color7==A[6] and color4==A[3]:
            color4=black
            color7=black
    if color7==A[6] and color9==A[8]:
            color7=black
            color9=black
    if color7==A[6] and color10==A[9]:
            color7=black
            color10=black
    if color7==A[6] and color8==A[7]:
            color7=black
            color8=black
##
    if color8==A[7] and color3==A[2]:     #nead timeng
            color8=black
            color3=black
    if color8==A[7] and color1==A[0]:
            color1=black
            color8=black
    if color8==A[7] and color2==A[1]:
            color2=black
            color8=black
    if color8==A[7] and color6==A[5]:
            color8=black
            color6=black
    if color8==A[7] and color5==A[4]:
            color5=black
            color8=black
    if color8==A[7] and color4==A[3]:
            color4=black
            color8=black
    if color8==A[7] and color9==A[8]:
            color8=black
            color9=black
    if color8==A[7] and color10==A[9]:
            color8=black
            color10=black
##
    if color9==A[8] and color3==A[2]:     #nead timeng
            color9=black
            color3=black
    if color9==A[8] and color1==A[0]:
            color1=black
            color9=black
    if color9==A[8] and color2==A[1]:
            color2=black
            color9=black
    if color9==A[8] and color6==A[5]:
            color9=black
            color6=black
    if color9==A[8] and color5==A[4]:
            color5=black
            color9=black
    if color9==A[8] and color4==A[3]:
            color4=black
            color9=black
    if color9==A[8] and color7==A[6]:
            color7=black
            color9=black
    if color9==A[8] and color8==A[7]:
            color8=black
            color9=black
    if color9==A[8] and color10==A[9]:
            color10=black
            color9=black
##
    if color10==A[9] and color3==A[2]:
            color10=black
            color3=black
    if color10==A[9] and color1==A[0]:
            color1=black
            color10=black
    if color10==A[9] and color2==A[1]:
            color2=black
            color10=black
    if color10==A[9] and color6==A[5]:
            color10=black
            color6=black
    if color10==A[9] and color5==A[4]:
            color5=black
            color10=black
    if color10==A[9] and color4==A[3]:
            color4=black
            color10=black
    if color10==A[9] and color7==A[6]:
            color7=black
            color10=black
    if color10==A[9] and color8==A[7]:
            color8=black
            color10=black

    pygame.display.flip()     #obnova ekrana
    clock.tick(15)           #tipa fps
pygame.quit()        #konec