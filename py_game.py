1231454877

import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
pygame.key.set_repeat(50)

fenetre = pygame.display.set_mode((1200, 800))

perso = pygame.image.load("po.gif").convert_alpha()


position_perso = perso.get_rect()

pas_deplacement = 15 

while True :

    for event in pygame.event.get() :
        position_perso.topleft = (randint(0,540),randint(0,380))
        fenetre.blit(perso, position_perso)
        pygame.display.flip()
        pygame.time.delay(50)


        fenetre.fill([255,0,0])
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
    
    print("je m'appelle Ahmed")
