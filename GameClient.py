# -*- coding: utf-8 -*-
import time
import pygame
import base
import Pyfighter
"""
Created on Sun Mar 30 15:22:18 2014

The Game Client class provides all needed functional requirements to play the
game.

@author: Will Stiles
@author: Diego Gonzalez
"""


class GameClient:
    """
        Creates a game client and initializes all of the items necessary to
        play the game.
    """
    def __init__(self):
        #   Initialize pygame

        self.player = Pyfighter.Pyfighter(1, "Carver")
        self.opponent = Pyfighter.Pyfighter(2, "Orc")
        """
            Initialize screen default color and level, size, and the rectangle
        """
        self.background = base.base() #
        self.background._init_("sounds/fight.mp3", "Level/Scene.jpg") #
        self.size = self.width, self.height = 800, 600 #
        #self.speed1 = [0, 0] #
        #self.speed2 = [0, 0] #
        self.black = 0, 0, 0 #
        #self.images1 = [] #
        self.image1Count = 0 #
        #self.images2 = [] #
        self.image2Count = 0 #
        self.back = self.background.getLevel()
        self.backRect = self.back.get_rect(center=(self.width/2,self.height/2))
        self.screen = self.background.getScreen()
        """
            Set up floating platforms
        """
        self.longPlat = pygame.image.load("Level/2hundredbar.gif").convert()
        self.plat1 = pygame.image.load("Level/hundredbar.gif").convert()
        self.plat2 = pygame.image.load("Level/hundredbar.gif").convert()
        # self.shortPlat1 = pygame.image.load("Level/fiftybar.gif").convert()
        # self.shortPlat2 = pygame.image.load("Level/fiftybar.gif").convert()
        # Platform Rectangles
        self.longPlatRect = self.longPlat.get_rect(center=(self.width/2, 7*self.height/8))
        self.plat1Rect = self.plat1.get_rect(center=(self.width/4, 2*self.height/3))
        self.plat2Rect = self.plat2.get_rect(center=(self.width - self.width/4, 2*self.height/3))
        
        """
            Set up HP boxes and health
        """
        self.player1HP = pygame.image.load("CarverHP/CarverHP13.gif").convert()
        self.p1HPRect = self.player1HP.get_rect(right=(self.width/8), top=(self.height/10))
        self.player2HP = pygame.image.load("OrcHP/OrcHP13.gif").convert()
        self.p2HPRect = self.player1HP.get_rect(left=(self.width-(self.width/8)), top=(self.height/10))
        self.p1HP = 130
        self.p2HP = 130
        """
            Initialize the Surfaces to hold character images and have a rectangle
            around each for collision purposes.
        """
        #self.player1 = pygame.image.load("CarverSprite/CarverStill.gif").convert()
        #self.player1Rect = self.player1.get_rect(bottom=(585), left=(100))
        #self.player2 = pygame.image.load("OrcSprite/OrcStill.gif").convert()
        #self.player2Rect = self.player2.get_rect(bottom=(585), right=(700))
        
        """
            Initialize character facings
        """
        #self.face1 = "right"
        #self.face2 = "left"
        #self.player2 = pygame.transform.flip(self.player2, 1, 0)
    
        """
            Jump counters, if jumpN is ever greater than 5, then jumpNMax = 1
        """
        self.jump1 = 0
        self.jump1Max = 0
        self.jump1Peak = 0
        self.jump1Double = 0
        self.onPlat = 0
        
        """
            Attack counters
        """
        self.p1Shooting = False
        self.p1ShotDirection = "right"
        self.p1ShotCount = 0
        self.p1Shot = pygame.image.load("CarverSprite/CarverShot.gif").convert()
        self.p1ShotRect = self.p1Shot.get_rect(center=(-50,-50))
        self.p1Melee = 0 
        self.p1ShotSpeed = [0,0]
        
        """
            Draw the first display and both characters
        """
        self.screen.blit(self.back, self.backRect)
        #self.screen.blit(self.player1, self.player1Rect)
        #self.screen.blit(self.player2, self.player2Rect)
        self.screen.blit(self.player.getCurrentImage(), self.player.getHitBox())
        self.screen.blit(self.opponent.getCurrentImage(), self.opponent.getHitBox())
        self.screen.blit(self.longPlat, self.longPlatRect)
        self.screen.blit(self.plat1, self.plat1Rect)
        self.screen.blit(self.plat2, self.plat2Rect)
        pygame.display.flip()
        
        """
            Victory conditions
        """
        self.whoWins = 0
        
        self.keys = None            

    """
        Handles the redrawing of the sprites and the stage, as well as
        the animations.
    """
    def render(self):
        if self.player.getSpeed()[1] != 0:
            self.player.setCurrentImage(1)# = pygame.image.load("CarverSprite/CarverJump.gif").convert()
        elif (self.keys[pygame.K_d] or self.keys[pygame.K_a]) and \
            not (self.keys[pygame.K_d] and self.keys[pygame.K_a]):
            if self.image1Count < 10:
                self.player.setCurrentImage(3)# = pygame.image.load("CarverSprite/CarverRun0.gif").convert()
                self.image1Count = self.image1Count + 1
            elif self.image1Count < 19:
                self.player.setCurrentImage(4)# = pygame.image.load("CarverSprite/CarverRun1.gif").convert()
                self.image1Count = self.image1Count + 1
            else:
                self.image1Count = 0
        else:
            self.player.setCurrentImage(0)# = pygame.image.load("CarverSprite/CarverStill.gif").convert()

        if self.keys[pygame.K_d]:
            self.player.setFace("right")
        elif self.keys[pygame.K_a]:
            self.player.setFace("left")
                    
        if self.player.getFace() == "left":
            self.player.setCurrentImage(pygame.transform.flip(self.player.getCurrentImage(), 1, 0))

        """
            Handle HP Bar change and Victory conditions
        """
        if self.p1HP > 0 and self.p2HP > 0:
            self.player1HP = pygame.image.load("CarverHP/CarverHP%d.gif" % (self.p1HP / 10)).convert() 
            self.player2HP = pygame.image.load("OrcHP/OrcHP%d.gif" % (self.p2HP / 10)).convert()
        else:
            if self.p1HP <= 0 and self.p2HP > 0:
                self.whoWins = 2
            elif self.p1HP > 0 and self.p2HP <= 0:
                self.whoWins = 1
            else:
                self.whoWins = 3

        self.p1ShotRect = self.p1ShotRect.move(self.p1ShotSpeed)
        self.player.setHitBox(self.player.getHitBox().move(self.player.getSpeed()))
        self.opponent.setHitBox(self.opponent.getHitBox().move(self.opponent.getSpeed()))
        self.screen.fill(self.black)
        self.screen.blit(self.back, self.backRect)
        self.screen.blit(self.longPlat, self.longPlatRect)
        self.screen.blit(self.plat1, self.plat1Rect)
        self.screen.blit(self.plat2, self.plat2Rect)
        #self.screen.blit(self.player1, self.player1Rect)
        #self.screen.blit(self.player2, self.player2Rect)
        self.screen.blit(self.p1Shot, self.p1ShotRect)
        self.screen.blit(self.player.getCurrentImage(), self.player.getHitBox())
        self.screen.blit(self.opponent.getCurrentImage(), self.opponent.getHitBox())
        self.screen.blit(self.player1HP, self.p1HPRect)
        self.screen.blit(self.player2HP, self.p2HPRect)
        pygame.display.flip()
        time.sleep(.01)

    """
        Moves players that are holding the left or right keys and changes
        faced direction when necessary.
    """
    def move(self):
        """
            Player 1 Movement
            Controls:
            A           = Left
            D           = Right
            Spacebar    = Jump (Double Jump Enabled on rise, not fall)
        """
        if self.keys[pygame.K_d]:
            self.player.setPyfighterX(3.5)
            if self.player.getFace() == "left":
                self.player.setFace("right")
                self.player.setFace(pygame.transform.flip(self.player.getCurrentImage(), 1, 0))
        if self.keys[pygame.K_a]:
            self.player.setPyfighterX(-3.5)
            if self.player.getFace() == "right":
                self.player.setFace("left")
                self.player.setFace(pygame.transform.flip(self.player.getCurrentImage(), 1, 0))
        if self.keys[pygame.K_a] and self.keys[pygame.K_d]:
            self.player.setPyfighterX(0)
        if self.keys[pygame.K_SPACE]:
            if self.jump1Max < 2:
                self.jump1 = 4
                self.jump1Peak = self.player.getHitBox().top - 100
            self.jump1Max = self.jump1Max + 1
        if not self.keys[pygame.K_a] and not self.keys[pygame.K_d]:
            self.player.setPyfighterX(0)
        """
            Player 2 Movement
            Controls:
                Left arrow  = Left
                Right arrow = Right
                (Jump Not Implemented)
        """
        if self.keys[pygame.K_RIGHT]:
            self.opponent.setPyfighterX(3.5)
            if self.opponent.getFace() == "left":
                self.opponent.setFace("right")
                self.opponent.setCurrentImage(pygame.transform.flip(self.opponent.getCurrentImage(), 1, 0))
        if self.keys[pygame.K_LEFT]:
            self.opponent.setPyfighterX(-3.5)
            if self.opponent.getFace() == "right":
                self.opponent.setFace("left")
                self.opponent.setCurrentImage(pygame.transform.flip(self.opponent.getCurrentImage(), 1, 0))
        if not self.keys[pygame.K_RIGHT] and not self.keys[pygame.K_LEFT]:
            self.opponent.setPyfighterX(0)


        if self.player.getHitBox().right + self.player.getSpeed()[0] > 785 or \
           self.player.getHitBox().left + self.player.getSpeed()[0] < 15:
            self.player.setPyfighterX(0)
        if self.opponent.getHitBox().right + self.opponent.getSpeed()[0] > 785 or \
           self.opponent.getHitBox().left + self.opponent.getSpeed()[0] < 15:
            self.opponent.setPyfighterX(0)
    
    """
        Checks for jumping and then sets the y coordinate of the player's speed
        to negative, causing it to rise.
    """
    def jump(self):
        """
            Jumping logic for Player 1
        """
        if self.jump1 > 0:
            self.jump1 -= 1
            self.player.setPyfighterY(-3)
        elif self.jump1 < 0:
            self.jump1 += 1
            self.player.setPyfighterY(3)
        elif self.jump1Max == 1:
            self.jump1 = -4
            self.player.setPyfighterY(0)
        """
            Collision avoidance
        """
        if self.player.getHitBox().bottom + self.player.getSpeed()[1] > 585 or \
           self.onPlatform(self.player.getHitBox()):
            self.onPlat = 1
            self.player.setPyfighterY(0)
            self.jump1Max = 0            
            self.jump1Double = 0         
        elif not self.onPlatform:
            self.player.setPyfighterY(3)

        if self.player.getHitBox().top + self.player.getSpeed()[1] < self.jump1Peak or \
           self.player.getHitBox().top + self.player.getSpeed()[1] < self.jump1Peak:
            self.player.setPyfighterY(0)
            self.jump1 = -4
    
    """
        Checks to see if the given PlayerRect is on top of a platform
        
        @param  playerRect  The Rect to check
    """        
    def onPlatform(self, playerRect):
        onPlat = False
        
        # Check if the player is on top of the 200 long platform
        if playerRect.bottom + self.player.getSpeed()[1] > self.longPlatRect.top and \
        playerRect.left < self.longPlatRect.right and \
        playerRect.right > self.longPlatRect.left and \
        playerRect.top + playerRect.height < self.longPlatRect.top:
            onPlat = True
        
        # Check if the player is on top of the left 100 long platform
        if playerRect.bottom + self.player.getSpeed()[1] < self.plat1Rect.top and \
        playerRect.left < self.plat1Rect.right and \
        playerRect.right > self.plat1Rect.left and \
        playerRect.top + playerRect.height > self.plat1Rect.top: 
            onPlat = True

        # Check if the player is on top of the right 100 long platform
        if playerRect.bottom + self.player.getSpeed()[1] < self.plat2Rect.top and \
        playerRect.left < self.plat2Rect.right and \
        playerRect.right > self.plat2Rect.left and \
        playerRect.top + playerRect.height < self.plat2Rect.top:
            onPlat = True
            
        return onPlat        
        
        
    
    """
        Checks for attacks and creates a Surface and rectangle around the
        Surface for an attack object.
    """
    def attack(self):
        if self.keys[pygame.K_j] and not self.p1Shooting:
            self.p1Shooting = self.keys[pygame.K_j]
            self.p1ShotCount = 0
        if self.p1ShotCount <= 25 and self.p1Shooting:
            if self.p1ShotCount == 0:
                self.p1ShotSpeed[0] = 8
                if self.player.getFace() == "left":
                    self.p1ShotSpeed[0] = self.p1ShotSpeed[0] * -1
                    self.p1ShotRect.right = self.player.getHitBox().left
                    self.p1ShotRect.centery = self.player.getHitBox().centery
                    if self.p1ShotDirection == "right":
                        self.p1ShotDirection = "left"
                        self.p1Shot = pygame.transform.flip(self.p1Shot, 1, 0)
                else:
                    self.p1ShotRect.left = self.player.getHitBox().right
                    self.p1ShotRect.centery = self.player.getHitBox().centery
                    if self.p1ShotDirection == "left":
                        self.p1ShotDirection = "right"
                        self.p1Shot = pygame.transform.flip(self.p1Shot, 1, 0)
            self.p1ShotCount = self.p1ShotCount + 1
        else:
            self.p1ShotRect.center = (-50, -50)
            self.p1ShotCount = 0
            self.p1Shooting = False
        
        """
            Check for hits
        """
        if self.p1ShotDirection == "right" and self.p1ShotRect.centerx + \
            self.p1ShotSpeed[0] >= self.opponent.getHitBox().left and \
            self.p1ShotRect.centerx < self.opponent.getHitBox().right and \
            self.p1ShotRect.centery < self.opponent.getHitBox().bottom and \
            self.p1ShotRect.centery > self.opponent.getHitBox().top:
                self.p2HP = self.p2HP - 5
                self.p1ShotRect.center = (-50, -50)
                self.p1ShotSpeed[0] = 0
                
    """
        Checks for a Victory
    """
    def ifWin(self):
        if self.whoWins != 0:
            return self.whoWins
