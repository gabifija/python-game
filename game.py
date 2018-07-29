import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

cat_width = 45
cat_height = 25

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Nyan Cat Race')
clock = pygame.time.Clock()

catImg = pygame.image.load('cat.png')
catImg = pygame.transform.scale(catImg, (cat_width,cat_height))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def cat(x,y):
    gameDisplay.blit(catImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('Oops!')

def game_loop():
    x = (display_width * 0.05)
    y = (display_height * 0.45)

    y_change = 0

    thing_startx = 1600
    thing_starty = random.randrange(0, display_height)
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

            print(event)

        y += y_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_startx -= thing_speed

        cat(x,y)

        if y > display_height-cat_height or y < 0:
            crash()

        if thing_startx < 0:
            thing_startx = display_width + thing_width
            thing_starty = random.randrange(0,display_height-thing_height)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
