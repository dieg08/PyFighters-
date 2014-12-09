import pygame, sys, InitScript, socket, errno, Menu, time
from socket import error as socket_error
import Tkinter, tkMessageBox


def charselect():
    pygame.init()
    white = (255, 255, 255)
    screen = pygame.display.get_surface()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    level = pygame.image.load("background/back2.jpg").convert()
    orc = pygame.image.load("background/orc.jpg").convert()
    carver = pygame.image.load("background/warrior.jpg").convert()
    myfont = pygame.font.Font("fonts/Sketch Gothic School.ttf", 100)
    ofont = pygame.font.Font("fonts/Sketch Gothic School.ttf", 40)
    title = "Select Player"
    player1 = "Orc"
    player2 = "Carver"
    wait = "Waiting..."
    label = myfont.render(title, 1, white)
    one_title = ofont.render(player1, 1, white)
    two_title = ofont.render(player2, 1, white)
    wait_title = ofont.render(wait, 1, white)
    waitpos = wait_title.get_rect()
    textpos = label.get_rect()
    orcpos = orc.get_rect()
    warpos = carver.get_rect()
    onepos = one_title.get_rect()
    twopos = two_title.get_rect()
    textpos.centerx = level.get_rect().centerx
    orcpos.centerx = level.get_rect().centerx - 100
    orcpos.centery = level.get_rect().centery
    warpos.centerx = level.get_rect().centerx + 100
    warpos.centery = level.get_rect().centery 
    onepos.centerx = orcpos.centerx 
    onepos.centery = orcpos.centery + 100
    twopos.centerx = warpos.centerx
    twopos.centery = warpos.centery + 100
    waitpos.centerx = textpos.centerx
    waitpos.centery = textpos.centery + 100
    pygame.event.clear()
    while 1:
        character = None    
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print str(pos)
                if orcpos.collidepoint(pos):
                    print "selected orc"
                    screen.blit(wait_title, waitpos)
                    pygame.display.flip()
                    time.sleep(3)
                    character = "Orc"
                elif warpos.collidepoint(pos):
                    print "selected carver"
                    screen.blit(wait_title, waitpos)
                    pygame.display.flip()
                    time.sleep(3)
                    character = "Carver"
            elif ev.type == pygame.KEYDOWN:
                keypressed = pygame.key.name(event.key)
                if keypressed == pygame.key.name(pygame.K_ESCAPE):
                    sys.exit(0)
        screen.blit(level, (0,0))
        screen.blit(orc, orcpos)
        screen.blit(carver, warpos)
        screen.blit(label, textpos)
        screen.blit(one_title, onepos)
        screen.blit(two_title, twopos)
        pygame.display.flip()
        if character != None:
            return character
    



