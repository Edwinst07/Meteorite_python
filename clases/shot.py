import pygame

class Missile(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.imageMissile = pygame.image.load("image/misil.png")
        self.rect = self.imageMissile.get_rect()
        self.velocityShot = 10
        self.rect.top = posY
        self.rect.left = posX

    def route(self):
        self.rect.top -= self.velocityShot

    def draw(self, surface):
        surface.blit(self.imageMissile, self.rect)