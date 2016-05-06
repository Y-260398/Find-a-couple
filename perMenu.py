# -*- coding: utf-8 -*-
import pygame, sys
import os

from pygame.locals  import *

pygame.font.init()

done=False
clock=pygame.time.Clock()

mx=[]
my=[]

xx=(750)
yy=(500)

f=open('testRandomv.2.py', 'r')

x1=(90)
y1=(90)
x2=(90)
y2=(170)
x3=(90)
y3=(260)

color1=(255,255,153)

font_color = (255, 255, 153)
highlite_color = (153, 102, 255)
font = pygame.font.Font(None, 72)
surface_width = 800
surface_height = 600

surface_menu = pygame.display.set_mode([surface_width,surface_height])

pygame.display.set_caption("Test")



image = pygame.image.load ("t.jpg").convert_alpha()


def DrawText(text, font, surface_menu, x, y, selected = False):
    	textobj = font.render(text, 1, font_color)
    	textrect = textobj.get_rect()
    	textrect.topleft = (x, y)
    	if selected:
    	    highlight = pygame.Surface((len(text) *33, 65))
    	    highlight.fill(highlite_color)
    	    surface_menu.blit(highlight, [x - 18, y - 15])
    	surface_menu.blit(textobj, textrect)
while not done:     #основной цикл программы
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

        if event.type==pygame.MOUSEBUTTONDOWN:          #говорим что будем использовать мышку
            if event.button==1:    #говорим чтоб он реагировал только на левую кнопку мыши... "1"-левая кнопка мышки
                    pos = pygame.mouse.get_pos()
                    mx = pos[0]                     #x мышки
                    my = pos[1]                     #y мышки

	DrawText('Start', font, image, x1, y1, True)
	DrawText('Info', font, image, x2, y2)
	DrawText('Exit', font, image, x3, y3)

    if mx != x1 and my != y1:
        f=open('testRandomv.2.py', 'r')
        # sys.exit()




    surface_menu.blit(image, (0,0))
    pygame.display.update()
    pygame.display.flip()     #obnova ekrana

pygame.display.update()