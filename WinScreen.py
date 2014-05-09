import pygame, sys, Menu

def winner(name):
    pygame.init()
    pygame.mixer.music.load("sounds/winscreen.mp3")
    pygame.mixer.music.play(-1)
    screen = pygame.display.get_surface()                                   
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE) 
    level = pygame.image.load("background/winScreen.jpg").convert()        
    levelRect = level.get_rect(center=(400, 300))
    screen.blit(level, (0, 0))
    myfont = pygame.font.Font("fonts/moonhouse.ttf", 50)
    winner = name + " Wins!!!"
    label = myfont.render(winner, 1, (0, 255, 0))
    textpos = label.get_rect()
    textpos.centerx = level.get_rect().centerx
    textpos.centery = level.get_rect().centery
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keypressed = pygame.key.name(event.key)
                if keypressed == pygame.key.name(pygame.K_ESCAPE):
                    Menu.main()
                    sys.exit(0)
        screen.blit(level, (0,0))
        screen.blit(label, textpos)
        pygame.display.flip()
