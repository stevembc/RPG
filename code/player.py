import pygame
from Data import *

class Player(pygame.sprite.Sprite):

    #Dfinitions du player 
    def __init__(self):
        super().__init__()

        #Caractéristique graphique
        self.surf = pygame.Surface((25,25)) #Taille du player
        self.surf.fill((110,84,184)) #Couleur du player
        self.rect = self.surf.get_rect(center = (WIDTH/2,HEIGHT/2))

        #Fluidité du mouvement
        self.pos = pygame.math.Vector2((WIDTH/2,HEIGHT/2))
        self.vel = pygame.math.Vector2((0,0)) # --> vélocitée = vitesse du player à un moment donnée (chute / saut)
        self.acc = pygame.math.Vector2((0,0)) # --> accélération

    #mouvement du player
    def Move(self): 
        self.acc.x = 0
        self.acc.y = 0

        pressed_key = pygame.key.get_pressed()      
        if pressed_key[pygame.K_LEFT]:
            self.acc.x = -ACC
            self.pos.x += -3

        if pressed_key[pygame.K_RIGHT]:
            self.acc.x = ACC
            self.pos.x += 3

        if pressed_key[pygame.K_UP]:
            self.acc.y = -ACC
            self.pos.y += -3

        if pressed_key[pygame.K_DOWN]:
            self.acc.y = ACC
            self.pos.y += 3

        self.acc.x += self.vel.x * FRICTION
        self.acc.y += self.vel.y * FRICTION
        self.vel += self.acc
        self.pos += self.vel

        #Le player ne peux pas sortir de la map    
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.y > WIDTH:
            self.pos.y = WIDTH

            
        self.rect.midbottom = (self.pos.x, self.pos.y)

    """def Collision(self,list_platform):
        hits = pygame.sprite.spritecollide(self ,list_platform , False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0"""