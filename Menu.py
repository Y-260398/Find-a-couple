# -*- coding: utf-8 -*-
import pygame, sys
import os

pygame.font.init()

done=False
clock=pygame.time.Clock()




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
    	    highlight = pygame.Surface((len(text) * 33, 65))
    	    highlight.fill(highlite_color)
    	    surface_menu.blit(highlight, [x - 18, y - 15])
    	surface_menu.blit(textobj, textrect)
while not done:     #основной цикл программы
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True


	DrawText('Start', font, image, (surface_width/5)-65, (surface_height/2)-110, True)
	DrawText('Options', font, image, (surface_width/5)-65, (surface_height/2)-40)
	DrawText('Quit', font, image, (surface_width/5)-65, (surface_height/2)+30)





    surface_menu.blit(image, (0,0))
    pygame.display.update()
    pygame.display.flip()     #obnova ekrana

pygame.display.update()