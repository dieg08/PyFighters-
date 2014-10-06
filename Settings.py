import pygame, Menu

def settings():
    pygame.init()
    screen = pygame.display.get_surface()                                       
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)              
    level = pygame.image.load("background/back2.jpg").convert()                
    levelRect = level.get_rect(center=(400, 300))       
    myfont = pygame.font.Font("fonts/moonhouse.ttf", 60)                        
    myfonta = pygame.font.Font(None, 30)                        
    myfontd = pygame.font.Font(None, 30)                        
    myfonts = pygame.font.Font(None, 30)                        
    myfontj = pygame.font.Font(None, 30)                        
    winner = "How to play" 
    a = 'A - This key moves your player left'
    d = 'D - This key moves your player right'
    space = 'Spacebar - This key makes your character jump'
    j = 'J - This key makes your character shoot'
    label = myfont.render(winner, 1, (0, 255, 0))
    labela = myfonta.render(a, 1, (255, 255, 0))
    labeld = myfontd.render(d, 1, (255, 255, 0))
    labels = myfonts.render(space, 1, (255, 255, 0))
    labelj = myfontj.render(j, 1, (255, 255, 0))
    textpos = label.get_rect()                                                  
    textposa = labela.get_rect()                                                  
    textposd = labeld.get_rect()                                                  
    textposs = labels.get_rect()                                                  
    textposj = labelj.get_rect()                                                  
    textpos.centerx = level.get_rect().centerx 
    textposa.centerx = level.get_rect().centerx 
    textposd.centerx = level.get_rect().centerx 
    textposs.centerx = level.get_rect().centerx 
    textposj.centerx = level.get_rect().centerx 
    textposa.centery = 200
    textposd.centery = 250
    textposs.centery = 300
    textposj.centery = 350
    while 1:                                                                    
        for event in pygame.event.get():                                        
            if event.type == pygame.KEYDOWN:                                    
                keypressed = pygame.key.name(event.key)                         
                if keypressed == pygame.key.name(pygame.K_ESCAPE):              
                    Menu.main()                                                 
                    sys.exit(0)                                                 
        screen.blit(level, (0,0))     
        screen.blit(label, textpos)
        screen.blit(labela, textposa)
        screen.blit(labeld, textposd)
        screen.blit(labels, textposs)
        screen.blit(labelj, textposj)
        pygame.display.flip() 
