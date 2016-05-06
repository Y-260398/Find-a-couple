import pygame
from pygame import *
import random
import time

x=750
y=500

size=(x,y)
red=(255,0,0)
red2=(255,0,0)
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,255)
blue2=(0,0,255)
ColorDK=(255,50,120)
ColorDK2=(255,50,120)
Fone=(150,180,200)
HZ=(200,250,190)
KZ=(250,250,60)
GB=(0,255,240)
GB2=(0,255,240)
RG=(255,240,0)
RG2=(255,240,0)
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
A=[red,red2,blue,blue2,ColorDK,ColorDK2,RG,RG2,GB,GB2]
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
                            color1=random.choice(A)
                    if (mx-x2<=wigth2 and mx-x2>=0) and (my-y2<=height2 and my-y2>=0):
                            color2=random.choice(A)
                    if (mx-x3<=wigth3 and mx-x3>=0) and (my-y3<=height3 and my-y3>=0):
                            color3=random.choice(A)
                    if (mx-x4<=wigth4 and mx-x4>=0) and (my-y4<=height4 and my-y4>=0):
                            color4=random.choice(A)
                    if (mx-x5<=wigth5 and mx-x5>=0) and (my-y5<=height5 and my-y5>=0):
                            color5=random.choice(A)
                    if (mx-x6<=wigth6 and mx-x6>=0) and (my-y6<=height6 and my-y6>=0):
                            color6=random.choice(A)
                    if (mx-x7<=wigth7 and mx-x7>=0) and (my-y7<=height7 and my-y7>=0):
                            color7=random.choice(A)
                    if (mx-x8<=wigth8 and mx-x8>=0) and (my-y8<=height8 and my-y8>=0):
                            color8=random.choice(A)
                    if (mx-x9<=wigth9 and mx-x9>=0) and (my-y9<=height9 and my-y9>=0):
                            color9=random.choice(A)
                    if (mx-x10<=wigth10 and mx-x10>=0) and (my-y10<=height10 and my-y10>=0):
                            color10=random.choice(A)




    screen.fill(Fone)
    a=pygame.draw.rect(screen,color1,[20,20,100,150],0)            #kvadrat1
    b=pygame.draw.rect(screen,color2,[20,250,100,150],0)
    c=pygame.draw.rect(screen,color3,[150,20,100,150],0)
    d=pygame.draw.rect(screen,color4,[150,250,100,150],0)
    e=pygame.draw.rect(screen,color5,[280,20,100,150],0)
    z=pygame.draw.rect(screen,color6,[280,250,100,150],0)
    q=pygame.draw.rect(screen,color7,[410,20,100,150],0)
    h=pygame.draw.rect(screen,color8,[410,250,100,150],0)
    p=pygame.draw.rect(screen,color9,[540,20,100,150],0)
    o=pygame.draw.rect(screen,color10,[540,250,100,150],0)



    if color1==random.choice(A) and color2==red:
           color1=Fone
           color2=Fone
    if color3==ColorDK and color6==ColorDK:
           color3=Fone
           color6=Fone
    if color4==blue and color5==blue:
           color4=Fone
           color5=Fone
    if color7==GB and color8==GB:           #destroyed
           color7=Fone
           color8=Fone
    if color9==RG and color10==RG:           #destroyed
           color9=Fone
           color10=Fone
##

    if color1==red and color3==ColorDK:     #nead timeng
            color1=black
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
    if color2==red and color3==ColorDK:     #nead timeng
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
    if color3==ColorDK and color2==red:     #nead timeng
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
    if color4==blue and color3==ColorDK:     #nead timeng
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
    if color5==blue and color3==ColorDK:     #nead timeng
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
    if color7==GB and color3==ColorDK:     #nead timeng
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
    if color8==GB and color3==ColorDK:     #nead timeng
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
    if color9==RG and color3==ColorDK:     #nead timeng
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
    if color10==RG and color3==ColorDK:     #nead timeng
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
    clock.tick(15)           #tipa fps
pygame.quit()        #konec