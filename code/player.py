import pygame

class Player(pygame.sprite.Sprite):

    #definitions du player (taille - position - couleur)
    def __init__(self):
        self.surf = pygame.Surface((25,25))
        self.surf.fill((110,84,184))
        self.rect = self.surf.get_rect(center = (576,350))
        self.pos = pygame.math.Vector2((576,350))

    #mouvement du player
    def Move(self):
        pressed_key = pygame.key.get_pressed()
        
        if pressed_key[pygame.K_q]:
            self.pos.x += -5
        if pressed_key[pygame.K_d]:
            self.pos.x += 5

        self.rect.center = (self.pos.x, self.pos.y)