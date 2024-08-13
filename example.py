from random import randint
from clases import spriteGroup
from pygame.locals import *
from time import perf_counter
import pygame, sys

WIDTH = 480
HEIGHT = 730

pygame.init()
backgroud = pygame.image.load("image/fondo.png")
window = pygame.display.set_mode((WIDTH, HEIGHT))
spriteG = spriteGroup.SpriteGroup(150,150)
images =[]
imageLoad = []

for n in range(10, 17):
    images.append("image/Explosion/Explosion_000"+str(n)+".png")

for n in range(0,7):
    imageLoad.append(pygame.image.load(images[n]))

sprites = pygame.sprite.Group()
sprites.add(spriteG)
clock = pygame.time.Clock()
while True:
    window.blit(backgroud, (0,0))

    
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            spriteG.explosion()

    sprites.draw(window)
    sprites.update(0.25)
    pygame.display.update()
    clock.tick(60)
