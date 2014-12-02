import pygame, sys, os, socket, errno, random, subprocess, time, InitScript, CharSelect, Settings, Script
from pygame.locals import *
from socket import error as socket_error
import Tkinter, tkMessageBox, Menu

class MenuItem (pygame.font.Font):
    '''
    The Menu Item should be derived from the pygame Font class
    '''
    def __init__(self, text, position, fontSize=50, antialias=1, color=(0, 0, 255), background=None):
        pygame.font.Font.__init__(self, "fonts/moonhouse.ttf", fontSize)
        self.text = text
        if background == None:
            self.textSurface = self.render(self.text, antialias, (0, 0, 255))
        else:
            self.textSurface = self.render(self.text, antialias, (0, 0, 255), background)

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
        size = width, height = 800, 600 
        screen = pygame.display.get_surface()
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)                    
        self.level = pygame.image.load("background/back2.jpg").convert()                              
        self.levelRect = self.level.get_rect(center=(width/2,height/2))
        self.active = False
        
        if pygame.font:
            fontSize = 36
            fontSpace = 4
            # loads the standard font with a size of 36 pixels
            # font = pygame.font.Font(None, fontSize)
            
            # calculate the height and startpoint of the menu
            # leave a space between each menu entry
            menuHeight = (fontSize + fontSpace) * len(menuEntries)
            startY = height / 2 - menuHeight / 2  
            
            # listOfTextPositions=list()
            self.menuEntries = list()
            for menuEntry in menuEntries:
                centerX = width / 2
                centerY = startY + fontSize + fontSpace
                newEnty = MenuItem(menuEntry, (centerX, centerY))
                self.menuEntries.append(newEnty)
                self.level.blit(newEnty.get_surface(), newEnty.get_pos())
                startY = startY + fontSize + fontSpace
                
        
            
    def drawMenu(self):
        self.active = True
    
        myfont = pygame.font.Font("fonts/moonhouse.ttf", 125)
        title = myfont.render("PyFighters", 1, (0, 255, 0))
        textpos = title.get_rect()
        textpos.centerx = self.level.get_rect().centerx
        screen = pygame.display.get_surface()
        screen.blit(self.level, (0, 0))
        screen.blit(title, textpos)
        
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

def socketInit():                                                               
    #Server IP and Port num                                                     
    host = '127.0.0.1'                                                          
    port = 6969                                                                 
    player = 1                                                                  
    #Try to create the socket and throw appropriate errs                        
    try:                                                                        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                   
    except socket.error, msg:                                                   
        print 'Failed to create a socket'                                       
        sys.exit()                                                              
    try:                                                                        
        remote_ip = socket.gethostbyname( host )                                
    except socket.gaierror:                                                     
        #could not resolve host                                                 
        print 'Hostname could not be resolved. Exiting'                         
        sys.exit()                                                              
    try:                                                                        
        s.connect((remote_ip, port))                                            
    except socket_error as serr:                                                
        if serr.errno != errno.ECONNREFUSED:                                    
            #not the error we're looking for                                    
            sys.exit()                                                          
        top = Tkinter.Tk()                                                      
        B1 = Tkinter.Button(top, text = "Connection Refused", command = popup)  
        B1.pack()                                                               
        top.mainloop()                                                          
        main()                                                             
    return s   

def popup():                                                                    
    tkMessageBox.showinfo("Warning", "Connection Refused") 

def main():
    # pygame initialization
    pygame.init()
    pygame.mixer.music.load('sounds/menu.mp3')
    pygame.mixer.music.play(-1)

    pygame.display.set_caption('PyFighters')
    pygame.mouse.set_visible(1)
    clock = pygame.time.Clock()
    
    
    
    
    # code for our menu 
    ourMenu = ("Play PyFighters",
               "Local Play",
               "How to play",
               "Statistics",
               "Exit")
    myMenu = Menu(ourMenu)
    myMenu.drawMenu()
    pygame.display.flip()
    # main loop for event handling and drawing
    while 1:
        clock.tick(60)

    # Handle Input Events
        for event in pygame.event.get():
            myMenu.handleEvent(event)
            # quit the game if escape is pressed
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == Menu.MENUCLICKEDEVENT:    
                if event.text == "Play PyFighters":
                    character = CharSelect.charselect()
                    print "Just Waiting..."
                    #time.sleep(3)
                    InitScript.main(socketInit(), character)
                elif event.text == "How to play":
                    Settings.settings()
                elif event.text == "Local Play":
                    Script.main()
                elif event.text == "Exit":
                    sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                myMenu.activate()
                sys.exit(0)

                
        if myMenu.isActive():
            myMenu.drawMenu()
               
        
        pygame.display.flip()
      
if __name__ == '__main__': main()
