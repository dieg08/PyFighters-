# -*- coding: utf-8 -*-
"""
This python program is only to simulate movement. This is not an actual part
of the game, it is the learning process to figure out how the mechanics
work.

@author: Will Stiles
@author: Diego Gonzalez
"""
import time, sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

carver = pygame.image.load("CarverStill.gif").convert()
carverRect = carver.get_rect()

"""
    Bouncing object around the screen.
"""
"""
For bouncing around a screen. --used to figure out motion
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    carverRect = carverRect.move(speed)
    if carverRect.left < 0 or carverRect.right > width:
        speed[0] = -speed[0]
    if carverRect.top < 0 or carverRect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(carver, carverRect)
    pygame.display.flip()
    time.sleep(.01)
"""

"""
    Basic movement mechanics
    
    Must do:
    --Next time around use the pygame.key.get_pressed() function to capture
        keys: Movement will be more fluent
    --Need to implement collision detection to keep from moving off edge of
        screen.
        - Add secondary objects and implement collision on them
        - Figure out how to control initial image placement
    --Need to implement swapping sprites using sprite sheets for sprite motion
        while translating
    
    Have done:    
    ++Implemented directional facing
    ++Basic character movement
"""
face = "right"
screen.fill(black)
screen.blit(carver, carverRect)
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keyname = pygame.key.name(event.key)
            print keyname
            if "w" == keyname and carverRect.top >= 0:
                speed[1] = -2
            elif "d" == keyname and carverRect.right < width:
                speed[0] = 2
                if face == "left":
                    carver = pygame.transform.flip(carver, 1, 0)
                    face = "right"
            elif "s" == keyname and carverRect.bottom < height:
                speed[1] = 2
            elif "a" == keyname and carverRect.left >= 0:
                speed[0] = -2
                if face == "right":
                    carver = pygame.transform.flip(carver, 1, 0)
                    face = "left"
        elif event.type == pygame.KEYUP:
            keyname = pygame.key.name(event.key)
            print keyname
            if "w" == keyname and carverRect.top >= 0:
                speed[1] = 0
            elif "d" == keyname and carverRect.right < width:
                speed[0] = 0
            elif "s" == keyname and carverRect.bottom < height:
                speed[1] = 0
            elif "a" == keyname and carverRect.left >= 0:
                speed[0] = 0
        elif event.type == pygame.QUIT: sys.exit()

    carverRect = carverRect.move(speed)
    screen.fill(black)
    screen.blit(carver, carverRect)
    pygame.display.flip()
    time.sleep(.01)


"""
    Using key_pressed(), for fluid movements, less bugs.
"""
"""
while running:
    keys = pygame.key.get_pressed
    """