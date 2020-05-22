# CMIS226 - Assignment 1
# Name: Ian Napier
# Project Name: Space Fighter
# Project Description: Space Fighter is an Asteroids clone.Players will rack up a score based on the amount of enemies and asteroids they destroy.

import pygame, sys
from pygame.locals import*

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Space Fighter Splash Page')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAROON = (128, 0, 0)
NAVY = (0, 0, 128)
OLIVE = (128, 128, 0)
GREEN = (0,200,0)

DISPLAYSURF.fill(WHITE)

font = pygame.font.SysFont('arielblack', 24)
font2 = pygame.font.SysFont('couriernew', 16)

course = font.render("CMIS226 Assignment 1", True, NAVY)
name = font.render("Ian Napier", True, MAROON)
title = font.render("Space Fighter", True, OLIVE)
desc1 = font2.render("Space Fighter is an Asteroids clone.", True, BLACK)
desc2 = font2.render("Players will rack up a score", True, BLACK)
desc3 = font2.render("based on the amount of enemies ", True, BLACK)
desc4 = font2.render("and asteroids they destroy ", True, BLACK)
desc5 = font2.render("Score will display upon completion", True, BLACK)




DISPLAYSURF.blit(course, (20, 20))
pygame.draw.line(DISPLAYSURF, NAVY, (20,55), (325, 55), 4)
DISPLAYSURF.blit(name, (20,70))
DISPLAYSURF.blit(title, (20,110))
DISPLAYSURF.blit(desc1, (20, 150))
DISPLAYSURF.blit(desc2, (20, 170))
DISPLAYSURF.blit(desc3, (20, 190))
DISPLAYSURF.blit(desc4, (20, 210))
DISPLAYSURF.blit(desc5, (20, 230))
pygame.draw.rect(DISPLAYSURF, OLIVE, (50, 250, 50, 25))



def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button():
    mouse = pygame.mouse.get_pos()
    if 50 + 50 > mouse[0] > 50 and 250 + 25 > mouse[1] > 250:
        pygame.draw.rect(DISPLAYSURF, GREEN, (50, 250, 50, 25))
    else:
        pygame.draw.rect(DISPLAYSURF, OLIVE, (50, 250, 50, 25))

    smallText = pygame.font.Font("freesansbold.ttf", 10)
    textSurf, textRect = text_objects("Start", smallText)
    textRect.center = ((50 + (50 / 2)), (250 + (25 / 2)))
    DISPLAYSURF.blit(textSurf, textRect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()

    mouse = pygame.mouse.get_pos()
    if 50 + 50 > mouse[0] > 50 and 250 + 25 > mouse[1] > 250:
        pygame.draw.rect(DISPLAYSURF, GREEN, (50, 250, 50, 25))
    else:
        pygame.draw.rect(DISPLAYSURF, OLIVE, (50, 250, 50, 25))

    smallText = pygame.font.Font("freesansbold.ttf", 10)
    textSurf, textRect = text_objects("Start", smallText)
    textRect.center = ( (50+(50/2)), (250+(25/2)) )
    DISPLAYSURF.blit(textSurf, textRect)

    pygame.display.update()


#scrolling background
#running
#jumping
