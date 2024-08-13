import pygame

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.imageAsteroid = pygame.image.load("image/Asteroid.png")
        self.rect = self.imageAsteroid.get_rect()
        self.velocity = 2
        self.rect.top = posY
        self.rect.left = posX
        self.listAsteroid = []

    def route(self):
        self.rect.top += self.velocity 
        
    def draw(self, surface):
        surface.blit(self.imageAsteroid, self.rect)
