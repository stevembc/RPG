import pygame
from player import Player
from platform import Platform


#loading
pygame.init()
frame_per_sec = pygame.time.Clock()
display_surface = pygame.display.set_mode((1152,700))

P = Player()
top = Platform()

#Left Platform
left = Platform()
left.surf = pygame.Surface((10,1152))
left.surf.fill((146,87,0))
left.rect = left.surf.get_rect(center = (5,576))
#Right Platform
right = Platform()
right.surf = pygame.Surface((10,1152))
right.surf.fill((146,87,0))
right.rect = right.surf.get_rect(center = (1147,576))
#Bot Platform
bot = Platform()
bot.surf = pygame.Surface((1152,10))
bot.surf.fill((146,87,0))
bot.rect = right.surf.get_rect(center = (576,695))

all_sprite = pygame.sprite.Group()
#Platform
all_sprite.add(P)
all_sprite.add(top)
all_sprite.add(left)
all_sprite.add(right)
all_sprite.add(bot)


#update
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    P.Move()
    display_surface.fill((20,20,0))

    for entity in all_sprite:
        display_surface.blit(entity.surf, entity.rect)

    pygame.display.update() 

    frame_per_sec.tick(60)