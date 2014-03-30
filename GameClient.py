# -*- coding: utf-8 -*-
import time, pygame
"""
Created on Sun Mar 30 15:22:18 2014

@author: Will Stiles
@author: Diego Gonzalez
"""
class GameClient:    
    def __init__(self):
        #   Initialize pygame
        pygame.init()
        """
            Initialize screen default color and level, size, and the rectangle
        """
        self.size = self.width, self.height = 800, 600
        self.speed1 = [0, 0]
        self.speed2 = [0, 0]
        self.black = 0, 0, 0

        self.screen = pygame.display.set_mode(self.size)
        self.level = pygame.image.load("Level/PyfightersStage1.gif").convert()
        self.levelRect = self.level.get_rect(center=(self.width/2,self.height/2))

        """
            Initialize the Surfaces to hold character images and have a rectangle
            around each for collision purposes.
        """
        self.player1 = pygame.image.load("CarverSprite/CarverStill.gif").convert()
        self.player1Rect = self.player1.get_rect(bottom=(585), left=(100))
        self.player2 = pygame.image.load("OrcSprite/OrcStill.gif").convert()
        self.player2Rect = self.player2.get_rect(bottom=(585), right=(700))
        
        """
            Initialize character facings
        """
        self.face1 = "right"
        self.face2 = "left"
        self.player2 = pygame.transform.flip(self.player2, 1, 0)
    
        """
            Jump counters, if jumpN is ever greater than 5, then jumpNMax = 1
        """
        self.jump1 = 0
        self.jump1Max = 0
        self.jump1Peak = 0
        self.jump1Double = 0
        """
            Draw the first display and both characters
        """
        self.screen.blit(self.level, self.levelRect)
        self.screen.blit(self.player1, self.player1Rect)
        self.screen.blit(self.player2, self.player2Rect)
        pygame.display.flip()
        
        self.keys = None            

    def render(self):
        self.player1Rect = self.player1Rect.move(self.speed1)
        self.player2Rect = self.player2Rect.move(self.speed2)
        self.screen.fill(self.black)
        self.screen.blit(self.level, self.levelRect)
        self.screen.blit(self.player1, self.player1Rect)
        self.screen.blit(self.player2, self.player2Rect)
        pygame.display.flip()
        time.sleep(.01)

    def move(self):
        """
            Player 1 Movement
            Controls:
            A           = Left
            D           = Right
            Spacebar    = Jump (Double Jump Enabled on rise, not fall)
        """
        if self.keys[pygame.K_d]:
            self.speed1[0] = 3.5
            if self.face1 == "left":
                self.face1 = "right"
                self.player1 = pygame.transform.flip(self.player1, 1, 0)
        if self.keys[pygame.K_a]:
            self.speed1[0] = -4
            if self.face1 == "right":
                self.face1 = "left"
                self.player1 = pygame.transform.flip(self.player1, 1, 0)
        if self.keys[pygame.K_SPACE]:
            if self.jump1Max < 2:
                self.jump1 = 4
            self.jump1Max = self.jump1Max + 1
        if not self.keys[pygame.K_a] and not self.keys[pygame.K_d]:
            self.speed1[0] = 0
        """
            Player 2 Movement
            Controls:
                Left arrow  = Left
                Right arrow = Right
                (Jump Not Implemented)
        """
        if self.keys[pygame.K_RIGHT]:
            self.speed2[0] = 4
            if self.face2 == "left":
                self.face2 = "right"
                self.player2 = pygame.transform.flip(self.player2, 1, 0)
        if self.keys[pygame.K_LEFT]:
            self.speed2[0] = -4
            if self.face2 == "right":
                self.face2 = "left"
                self.player2 = pygame.transform.flip(self.player2, 1, 0)
        if not self.keys[pygame.K_RIGHT] and not self.keys[pygame.K_LEFT] :
            self.speed2[0] = 0
        if self.player1Rect.right + self.speed1[0] > 785 or \
           self.player1Rect.left + self.speed1[0] < 15:
            self.speed1[0] = 0
        if self.player2Rect.right + self.speed2[0] > 785 or \
           self.player2Rect.left + self.speed2[0] < 15:
            self.speed2[0] = 0

    def jump(self):
        """
            Jumping logic for Player 1
        """
        if self.jump1 > 0:
            self.jump1 = self.jump1 - 1
            self.speed1[1] = -3
        elif self.jump1 < 0:
            self.jump1 = self.jump1 + 1
            self.speed1[1] = 3
        elif self.jump1Max == 1:
            self.jump1 = -4
            self.speed1[1] = 0
        if self.player1Rect.bottom + self.speed1[1] > 585:
            self.speed1[1] = 0
            self.jump1Max = 0            
            self.jump1Double = 0
        if self.player1Rect.top + self.speed1[1] < self.jump1Peak:
            self.speed1[1] = 0
            self.jump1 = -4