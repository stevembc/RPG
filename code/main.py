import pygame
from Data import * 
from player import Player
from platform import Platform


#loading
pygame.init()
frame_per_sec = pygame.time.Clock()
pygame.display.set_caption("Aisuhea")
display_surface = pygame.display.set_mode((WIDTH,HEIGHT))

background = pygame.image.load('images/map/map_end.jpg')
P = Player()
bot = Platform()

#Left Platform
left = Platform()
left.surf = pygame.Surface((10,HEIGHT))
left.surf.fill((146,87,0))
left.rect = left.surf.get_rect(midleft = (0,HEIGHT/2))
#Right Platform
right = Platform()
right.surf = pygame.Surface((10,HEIGHT))
right.surf.fill((146,87,0))
right.rect = right.surf.get_rect(midright = (WIDTH,HEIGHT/2))
#Top Platform
"""top = Platform()
   top.surf = pygame.Surface((1152,10))
   top.surf.fill((146,87,0))
   top.rect = right.surf.get_rect(center = (576,695))"""

all_sprite = pygame.sprite.Group()
#Platform
all_sprite.add(P)
all_sprite.add(bot)
all_sprite.add(left)
all_sprite.add(right)
#all_sprite.add(top)

"""#ajout des platforms de collisions
Platforms = pygame.sprite.Group()
Platforms.add(bot)
Platforms.add(left)
Platforms.add(right)"""

#update
while True:

    #Background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    P.Move()

    #P.Collision()
    display_surface.fill((20,20,0))
    display_surface.blit(background, (0,0))
    pygame.display.flip()

    for entity in all_sprite:
        display_surface.blit(entity.surf, entity.rect)

    pygame.display.update() 

    frame_per_sec.tick(60)