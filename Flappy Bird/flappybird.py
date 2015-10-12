import pygame
from pygame.locals import *
import random
import time

pygame.init()

displayWidth = 800
displayHeight = 600
player_position = (200,50)

size = (displayWidth, displayHeight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FLAPPY BIRD")

RED = (255, 0, 0)
BLACK = (0, 0, 0)
white = (255,255,255)
LBLUE = (0, 200, 255)

done = False
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
background_image = pygame.image.load("bkgrnd.png").convert()
bird_image = pygame.image.load("bird.png").convert()
bird_image.set_colorkey(white)
    
x = 400
y = 300
x_speed = 5
y_speed = 1


while not done == True:

    if player_position[1] > 550 :
        done = True
        
    x += x_speed

    if x> 750 or x < 0:
        x_speed *= -1

    y_speed += 1
    y += y_speed
    player_position=(x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_speed -= 20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                y_speed = 5
                
        


    screen.fill(LBLUE)
    screen.blit(background_image, [0,0])
    
    screen.blit(bird_image, [x,y])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
