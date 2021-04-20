import pygame

class Platform (pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface((1152,10))
        self.surf.fill((146,87,0))
        self.rect = self.surf.get_rect(center = (576,350))
