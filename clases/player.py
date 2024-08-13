import pygame
from clases import shot

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageShip = pygame.image.load("image/Ship.png").convert_alpha()
        self.imageExplosion = pygame.image.load("image/naveExplota.png")
        self.rect = self.imageShip.get_rect()
        self.rect.centerx = 240
        self.rect.centery = 690
        self.velocity = 2
        self.live = True
        self.listShot = []
    
    def move(self):
        if self.live:
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rect.right >490:
                self.rect.right = 490

    def shoot(self,x ,y):
        if self.live:
            missile =  shot.Missile(x, y)
            self.listShot.append(missile)
    
    def draw(self, surface):
        if self.live:
            surface.blit(self.imageShip, self.rect)
        else:
            surface.blit(self.imageExplosion, self.rect)
