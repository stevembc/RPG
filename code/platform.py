import pygame

#Platforme Top
class Platform (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((1152,10))
        self.surf.fill((146,87,0))
        self.rect = self.surf.get_rect(center = (5,576))

"""
#platform left
class Platform_G (pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((10,1152))
        self.surf.fill((146,87,0))
        self.rect = self.surf.get_rect(center = (5,576))

#Platform right
class Platform_D (pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((10,1152))
        self.surf.fill((146,87,0))
        self.rect = self.surf.get_rect(center = (1147,576))

#Platforme Bottom
class Platform_B (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((1152,10))
        self.surf.fill((146,87,0))
        self.rect = self.surf.get_rect(center = (576,695))
"""