import pygame, sys
from pygame.locals import *
from clases import asteroid
from clases import player
from clases import spriteGroup
from random import randint
from time import perf_counter

WIDTH = 480
HEIGHT = 730

spritesG = pygame.sprite.Group()
explosion = spriteGroup.SpriteGroup(150, 150)
spritesG.add(explosion)
clock = pygame.time.Clock()

playing = True
listAsteroid = []
#Font text
point = 0
size = 14
typeFountain = "Consolas"
string =f'Points: '
colorText = (255,255,255)

def loadAsteroid(x, y):
    meteorite = asteroid.Asteroid(x, y)
    listAsteroid.append(meteorite)

def gameOver():
    global playing
    playing = False
    for asteroid in listAsteroid:
        listAsteroid.remove(asteroid)

def meteorite():
    pygame.init()
    #Display
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    backgroud = pygame.image.load("image/fondo.png")
    #title
    pygame.display.set_caption("Meteorite")

    #Sounds
    pygame.mixer.music.load("sounds/music_background.wav")
    soundCollision = pygame.mixer.Sound("sounds/explosion_sound.wav")
    soundShot = pygame.mixer.Sound("sounds/laser_shot.wav")
    pygame.mixer.music.play(3)
    ship = player.Ship()

    count = 0
    while True:
        window.blit(backgroud, (0,0))
        ship.draw(window)
        #Font
        global point
        fountain = pygame.font.SysFont(typeFountain, size)
        text = fountain.render(string+str(point), True, colorText)
        window.blit(text, (0,0))

        time = perf_counter()
        if time - count > 1:
            count = time 
            posX = randint(2, 478)
            loadAsteroid(posX,0)

        if len(listAsteroid) > 0:
            for x in listAsteroid:
                if ship.live:
                    x.draw(window)
                    x.route()
                if x.rect.top > HEIGHT:
                    listAsteroid.remove(x)
                else:
                    if x.rect.colliderect(ship.rect):
                        listAsteroid.remove(x)
                        soundCollision.play()
                        ship.live = False
                        gameOver()

        #Shot missile
        if len(ship.listShot) > 0:
            if playing:
                for x in ship.listShot:
                    x.draw(window)
                    x.route()
                    if x.rect.top < -10:
                        ship.listShot.remove(x)
                    else:
                        for asteroid in listAsteroid:
                            if x.rect.colliderect(asteroid.rect):
                                listAsteroid.remove(asteroid)
                                ship.listShot.remove(x)
                                point +=1
                                #gameOver
        ship.move()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE: 
                    soundShot.play()
                    x,y = ship.rect.center
                    ship.shoot(x, y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] :
            if ship.live:
                ship.rect.left -= ship.velocity
        if keys[pygame.K_RIGHT]:
            if ship.live:
                ship.rect.right += ship.velocity
        
        if playing == False:
            fountainGameOver = pygame.font.SysFont(typeFountain, 40)
            #textGameOver = fountainGameOver.render(f"Game over", True, colorText)    
            #window.blit(textGameOver, (140, 350))  
            explosion.explosion()
            spritesG.draw(window)
            spritesG.update(0.25)
            pygame.mixer.music.fadeout(3000)
            

        pygame.display.flip()
        clock.tick(60)

meteorite()