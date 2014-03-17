import pygame, sys, os, random, subprocess, time
from pygame.locals import * 

class MenuItem (pygame.font.Font):
    '''
    The Menu Item should be derived from the pygame Font class
    '''
    def __init__(self, text, position, fontSize=36, antialias=1, color=(255, 255, 255), background=None):
        pygame.font.Font.__init__(self, None, fontSize)
        self.text = text
        if background == None:
            self.textSurface = self.render(self.text, antialias, (255, 255, 255))
        else:
            self.textSurface = self.render(self.text, antialias, (255, 255, 255), background)

        self.position = self.textSurface.get_rect(centerx=position[0], centery=position[1])
    def get_pos(self):
        return self.position
    def get_text(self):
        return self.text
    def get_surface(self):
        return self.textSurface
    

class Menu:
    '''
    The Menu should be initalized with a list of menu entries
    it then creates a menu accordingly and manages the different
    print Settings needed
    '''
    
    MENUCLICKEDEVENT = USEREVENT + 1
    
    def __init__(self, menuEntries, menuCenter=None):
        '''
        The constructer uses a list of string for the menu entries,
        which need  to be created
        and a menu center if non is defined, the center of the screen is used
        '''
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.background = pygame.Surface(screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.active = False
        
        if pygame.font:
            fontSize = 36
            fontSpace = 4
            # loads the standard font with a size of 36 pixels
            # font = pygame.font.Font(None, fontSize)
            
            # calculate the height and startpoint of the menu
            # leave a space between each menu entry
            menuHeight = (fontSize + fontSpace) * len(menuEntries)
            startY = self.background.get_height() / 2 - menuHeight / 2  
            
            # listOfTextPositions=list()
            self.menuEntries = list()
            for menuEntry in menuEntries:
                centerX = self.background.get_width() / 2
                centerY = startY + fontSize + fontSpace
                newEnty = MenuItem(menuEntry, (centerX, centerY))
                self.menuEntries.append(newEnty)
                self.background.blit(newEnty.get_surface(), newEnty.get_pos())
                startY = startY + fontSize + fontSpace
                
        
            
    def drawMenu(self):
        self.active = True            
        screen = pygame.display.get_surface()
        screen.blit(self.background, (0, 0))
        
    def isActive(self):
        return self.active
    def activate(self,):
        self.active = True
    def deactivate(self):
        self.active = False
    def handleEvent(self, event):
        # only send the event if menu is active
        if event.type == MOUSEBUTTONDOWN and self.isActive():
            # initiate with menu Item 0
            curItem = 0
            # get x and y of the current event 
            eventX = event.pos[0]
            eventY = event.pos[1]
            # for each text position 
            for menuItem in self.menuEntries:
                textPos = menuItem.get_pos()
                # check if current event is in the text area 
                if eventX > textPos.left and eventX < textPos.right \
                and eventY > textPos.top and eventY < textPos.bottom:
                    # if so fire new event, which states which menu item was clicked                        
                    menuEvent = pygame.event.Event(self.MENUCLICKEDEVENT, item=curItem, text=menuItem.get_text())
                    pygame.event.post(menuEvent)
                curItem = curItem + 1
                
def nextScreen():
    pygame.mixer.music.load('02 Banish From Sanctuary.mp3')
    pygame.mixer.music.play(0)    
    size = width, height = 800, 600
    speed1 = [0, 0]
    speed2 = [0, 0]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    player1 = pygame.image.load("CarverSprite/CarverStill.gif").convert()
    player1Rect = player1.get_rect(center=(100,550))
    player2 = pygame.image.load("OrcSprite/OrcStill.gif").convert()
    player2Rect = player2.get_rect(center=(700, 550))
        
    face1 = "right"
    face2 = "left"
    player2 = pygame.transform.flip(player2, 1, 0)
    screen.fill(black)
    screen.blit(player1, player1Rect)
    screen.blit(player2, player2Rect)
    pygame.display.flip()
        
    keys = None
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            speed1[0] = 2
            if face1 == "left":
                face1 = "right"
                player1 = pygame.transform.flip(player1, 1, 0)
        if keys[pygame.K_a]:
            speed1[0] = -2
            if face1 == "right":
                face1 = "left"
                player1 = pygame.transform.flip(player1, 1, 0)
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            speed1 = [0, 0]
        if keys[pygame.K_RIGHT]:
            speed2[0] = 2
            if face2 == "left":
                face2 = "right"
                player2 = pygame.transform.flip(player2, 1, 0)
        if keys[pygame.K_LEFT]:
            speed2[0] = -2
            if face2 == "right":
                face2 = "left"
                player2 = pygame.transform.flip(player2, 1, 0)
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] :
            speed2 = [0, 0]
        if player1Rect.right + speed1[0] > 800 or \
           player1Rect.left + speed1[0] < 0:
            speed1 = [0, 0]
        if player2Rect.right + speed2[0] > 800 or \
           player2Rect.left + speed2[0] < 0:
            speed2 = [0, 0]
        player1Rect = player1Rect.move(speed1)
        player2Rect = player2Rect.move(speed2)
        screen.fill(black)
        screen.blit(player1, player1Rect)
        screen.blit(player2, player2Rect)
        pygame.display.flip()
        time.sleep(.01)

def main():
    # pygame initialization
    width = 800
    height = 600

    pygame.init()
    pygame.mixer.music.load('8bp107-01-linde-galileon.mp3')
    pygame.mixer.music.play(0)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('PyFighters')
    pygame.mouse.set_visible(1)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    #background = pygame.image.load("snake.jpg")
    background.fill((0, 0, 0))
    clock = pygame.time.Clock()
    
    
    
    # draw background
    img = pygame.image.load("snake.jpg").convert()
    screen.blit(img, (0, 0))
    pygame.display.update()
    
    # code for our menu 
    ourMenu = ("Play PyFighters",
               "How to play",
               "Statistics",
               "Exit")
 
    myMenu = Menu(ourMenu)
    myMenu.drawMenu()
  #  pygame.display.flip()
    # main loop for event handling and drawing
    while 1:
        clock.tick(60)

    # Handle Input Events
        for event in pygame.event.get():
            myMenu.handleEvent(event)
            # quit the game if escape is pressed
            if event.type == QUIT:
                return
            elif event.type == Menu.MENUCLICKEDEVENT:    
                if event.text == "Play PyFighters":
                    #subprocess.Popen(["python2.7", "movementtests.py"])
                    nextScreen()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                myMenu.activate()
            elif event.type == Menu.MENUCLICKEDEVENT:
                if event.text == "Exit":
                    return
                elif event.item == 0:
                    isGameActive = True
                    myMenu.deactivate()
            
                
        #img = pygame.image.load("sam.jpg").convert()
        #subprocess.Popen(["python2.7", "movementtests.py"])
        screen.blit(background, (0, 0))    
        if myMenu.isActive():
            myMenu.drawMenu()
        else:
            background.fill((0, 0, 0))
               
        
        pygame.display.flip()
      
if __name__ == '__main__': main()
