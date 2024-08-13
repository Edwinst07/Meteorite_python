import pygame

class SpriteGroup(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.boom = False
        self.spr = []
        img =[]
        for n in range(10, 99):
            img.append("image/Explosion/Explosion_000"+str(n)+".png")
        for image in img:
            self.spr.append(pygame.image.load(image))
        self.sprites = self.spr
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [posX, posY]
        #self.image = pygame.image.load()
        #self.rect = self.image.get_rect()
        #self.rect.x = posX
        #self.rect.y = posY

    def addImages(self):
        img =[]
        for n in range(10, 99):
            img.append("image/Explosion/Explosion_000"+str(n)+".png")
            
        for image in img:
            self.spr.append(pygame.image.load(image))
        
        
        
    def explosion(self):
        self.boom = True

    def update(self, speed):
        if self.boom:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.boom = False 
        self.image = self.sprites[int(self.current_sprite)]

        

        
