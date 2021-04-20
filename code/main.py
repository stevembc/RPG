import pygame
from player import Player
from plateforme import Platform

#loading
pygame.init()
frame_per_sec = pygame.time.Clock()
display_surface = pygame.display.set_mode((1152,700))

P = Player()
lvl1 = Platform()

#update
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    P.Move()

    display_surface.fill((20,20,0))
    display_surface.blit(P.surf,P.rect)
    display_surface.blit(lvl1.surf,lvl1.rect)
    pygame.display.update() 

    frame_per_sec.tick(60)