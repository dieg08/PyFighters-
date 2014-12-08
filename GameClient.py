# -*- coding: utf-8 -*-
import time
import pygame
import Platform
import Pyfighter
import Stage
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
    def __init__(self, playerNum, character):
        # Black color
        self.black = 0, 0, 0
        # Set screen dimensions
        self.size = self.width, self.height = 800, 600
        # Initialize Pygame
        pygame.init()
        # Create the screen display
        self.screen = pygame.display.get_surface()
        # Set the screen size
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        # Initialize the Pyfighters
        self.__initCharacters(playerNum, character)
        # Create the stage
        self.__createStage()
        # Player's current image
        self.image1Count = 0
        # Opponent's current image
        self.image2Count = 0
        # The background of the game
        self.back = self.stage.getLevel()
        # The bounds of the game screen
        self.backRect = self.stage.getLevelRect()
        # Set up HP bars and health
        self.__createHpBars()
        self.p1HP = 130
        self.p2HP = 130
        # Initialize jump counters for the player
        self.__initJumpCounters()
        # Initialize attack counters
        self.__initAttackCounters(self.playerChar)
        # First render
        self.__initialRender()
        # Victory conditions
        self.whoWins = 0
        # Initialize keys pressed
        self.keys = None

    """
        Create the stage
    """
    def __createStage(self):
        self.centerPlat = Platform.Platform("Level/2hundredbar.gif",
                                            center=(self.width/2, 7*self.height/8))
        self.leftPlat = Platform.Platform("Level/hundredbar.gif",
                                          center=(self.width/4, 3*self.height/4))
        self.rightPlat = Platform.Platform("Level/hundredbar.gif",
                                           center=(self.width - self.width/4, 3*self.height/4))
        self.stage = Stage.Stage("sounds/fight.mp3", "Level/Scene.jpg", self.width, self.height,
                                 self.centerPlat, self.leftPlat, self.rightPlat)

    """
        Create the HP bars on the screen
    """
    def __createHpBars(self):
        self.player1HP = pygame.image.load("CarverHP/CarverHP13.gif").convert()
        self.p1HPRect = self.player1HP.get_rect(right=(self.width/8), top=(self.height/10))
        self.player2HP = pygame.image.load("OrcHP/OrcHP13.gif").convert()
        self.p2HPRect = self.player1HP.get_rect(left=(self.width-(self.width/8)), top=(self.height/10))

    """
        Initialize Pyfighters
    """
    def __initCharacters(self, playerNum, character):
        self.playerChar = character[0]
        self.opponentChar = character[1]
        self.player = None
        self.opponent = None
        if playerNum == 1:
            self.player = Pyfighter.Pyfighter(playerNum, character[playerNum - 1])
            self.opponent = Pyfighter.Pyfighter(playerNum, character[playerNum])
            self.playerChar = character[playerNum - 1]
            self.opponentChar = character[playerNum]
            self.opponent.setCurrentImage(pygame.transform.flip(self.opponent.getCurrentImage(), 1, 0))
        elif playerNum == 2:
            self.player = Pyfighter.Pyfighter(playerNum, character[playerNum - 1])
            self.opponent = Pyfighter.Pyfighter(playerNum, character[playerNum - 2])
            self.playerChar = character[playerNum - 1]
            self.opponentChar = character[playerNum - 2]
            self.opponent.setCurrentImage(pygame.transform.flip(self.opponent.getCurrentImage(), 1, 0))

    """
        Initialize the jump counters for the player
        Jump counters, if jumpN is ever greater than 5, then jumpNMax = 1
    """
    def __initJumpCounters(self):
        self.jump1 = 0
        self.jump1Max = 0
        self.jump1Peak = 0
        self.jump1Double = 0
        self.onPlat = 0

    """
        Draw the first display and both characters
    """
    def __initialRender(self):
        self.screen.blit(self.back, self.backRect)
        self.screen.blit(self.player.getCurrentImage(), self.player.getHitBox())
        self.screen.blit(self.opponent.getCurrentImage(), self.opponent.getHitBox())
        self.screen.blit(self.centerPlat.getPlat(), self.centerPlat.getRect())
        self.screen.blit(self.leftPlat.getPlat(), self.leftPlat.getRect())
        self.screen.blit(self.rightPlat.getPlat(), self.rightPlat.getRect())
        pygame.display.flip()

    """
        Initialize the attach counters for the player
    """
    def __initAttackCounters(self, character):
        self.p1Shooting = False
        self.p1ShotDirection = "right"
        self.p1ShotCount = 0
        self.p1Shot = pygame.image.load(character + "Sprite/" + character + \
                                        "Shot.gif").convert()
        self.p2Shot = pygame.image.load(self.opponentChar + "Sprite/" + \
                                        self.opponentChar + "Shot.gif").convert()
        self.p2ShotRect = self.p2Shot.get_rect(center=(-50,-50))
        self.p1ShotRect = self.p1Shot.get_rect(center=(-50,-50))
        self.p1Melee = 0
        self.p1ShotSpeed = [0, 0]

    """
        Handles the redrawing of the sprites and the stage, as well as
        the animations.
    """
    def render(self, oppKeys):
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

        # Animate opponent's Pyfighter
        self.__animateOpponent(self.opponent, oppKeys)

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

        # Draw to the screen
        self.__blit()
        time.sleep(.01)

    """
        Draw all objects to the screen
    """
    def __blit(self):
        # Draw
        self.p1ShotRect = self.p1ShotRect.move(self.p1ShotSpeed)
        self.player.setHitBox(self.player.getHitBox().move(self.player.getSpeed()).center)
        self.opponent.setHitBox(self.opponent.getHitBox().move(self.opponent.getSpeed()).center)
        self.screen.fill(self.black)
        self.screen.blit(self.back, self.backRect)
        self.screen.blit(self.centerPlat.getPlat(), self.centerPlat.getRect())
        self.screen.blit(self.leftPlat.getPlat(), self.leftPlat.getRect())
        self.screen.blit(self.rightPlat.getPlat(), self.rightPlat.getRect())
        #self.screen.blit(self.player1, self.player1Rect)
        #self.screen.blit(self.player2, self.player2Rect)
        self.screen.blit(self.p1Shot, self.p1ShotRect)
        self.screen.blit(self.p2Shot, self.p2ShotRect)
        self.screen.blit(self.player.getCurrentImage(), self.player.getHitBox())
        self.screen.blit(self.opponent.getCurrentImage(), self.opponent.getHitBox())
        self.screen.blit(self.player1HP, self.p1HPRect)
        self.screen.blit(self.player2HP, self.p2HPRect)
        pygame.display.flip()

    """
        Moves players that are holding the left or right keys and changes
        faced direction when necessary.
    """
    def move(self, oppCenter):
        # Perform possible player movements
        self.__movePlayer(self.player)
        # Move the online opponent
        self.__moveOpponent(self.opponent, oppCenter)

        # Prevent moving through walls
        self.__walled(self.player)
        self.__walled(self.opponent)

    def __walled(self, player):
        if player.getHitBox().right + player.getSpeed()[0] > 785 or \
           player.getHitBox().left + player.getSpeed()[0] < 15:
            player.setPyfighterX(0)

    """
        Player 1 Movement
        Controls:
        A           = Left
        D           = Right
        Spacebar    = Jump (Double Jump Enabled on rise, not fall)
    """
    def __movePlayer(self, player):
        if self.keys[pygame.K_d]:
            self.player.setPyfighterX(3.5)
            if self.player.getFace() == "left":
                self.player.setFace("right")
                #self.player.setFace(pygame.transform.flip(self.player.getCurrentImage(), 1, 0))
        if self.keys[pygame.K_a]:
            self.player.setPyfighterX(-3.5)
            if self.player.getFace() == "right":
                self.player.setFace("left")
                #self.player.setFace(pygame.transform.flip(self.player.getCurrentImage(), 1, 0))
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
        Move the opponent based on the information from the server/AI controller

        @param  player  The player to move
        @param  center  The center of the hitbox of the opponent
    """
    def __moveOpponent(self, player, center):
        x = center[0]
        y = center[1]
        player.setHitBox((x, y))

    """
        Check for opponent attacks

        @param opponent The opponent
    """
    def opponentAttack(self, player):
        #TODO
        return

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
           self.onPlatform(self.player.getHitBox(), self.player):
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
    def onPlatform(self, playerRect, player):
        onPlat = False
        if not onPlat:
            onPlat = self.centerPlat.checkStanding(player)
        elif not onPlat:
            onPlat = self.leftPlat.checkStanding(player)
        else:
            onPlat = self.rightPlat.checkStanding(player)
        
        # Check if the player is on top of the 200 long platform
        #if playerRect.bottom + self.player.getSpeed()[1] > self.longPlatRect.top and \
        #playerRect.left < self.longPlatRect.right and \
        #playerRect.right > self.longPlatRect.left and \
        #playerRect.top + playerRect.height < self.longPlatRect.top:
        #    onPlat = True
        
        # Check if the player is on top of the left 100 long platform
        #if playerRect.bottom + self.player.getSpeed()[1] < self.plat1Rect.top and \
        #playerRect.left < self.plat1Rect.right and \
        #playerRect.right > self.plat1Rect.left and \
        #playerRect.top + playerRect.height > self.plat1Rect.top:
        #    onPlat = True

        # Check if the player is on top of the right 100 long platform
        #if playerRect.bottom + self.player.getSpeed()[1] < self.plat2Rect.top and \
        #playerRect.left < self.plat2Rect.right and \
        #playerRect.right > self.plat2Rect.left and \
        #playerRect.top + playerRect.height < self.plat2Rect.top:
        #    onPlat = True
            
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

        # Check for hits
        self.ifHit()

    """
        Check for hits
    """
    def ifHit(self):
        if self.p1ShotDirection == "right":
            if self.p1ShotRect.centerx + self.p1ShotSpeed[0] >= \
               self.opponent.getHitBox().left:
                if self.p1ShotRect.centerx < self.opponent.getHitBox().right and \
                   self.p1ShotRect.centery < self.opponent.getHitBox().bottom and \
                   self.p1ShotRect.centery > self.opponent.getHitBox().top:
                    self.p2HP = self.p2HP - 5
                    self.p1ShotRect.center = (-50, -50)
                    self.p1ShotSpeed[0] = 0


    """
        Animate opponent based on keys pressed by the opponent

        @param  player      The Pyfighter of the opponent
        @param  keys        The keys pressed by the oppponent
    """
    def __animateOpponent(self, player, keys):
        if player.getSpeed()[0] != 0:#not self.onPlatform(player.getHitBox(), player):
            player.setCurrentImage(1)# = pygame.image.load("CarverSprite/CarverJump.gif").convert()
        elif (keys[pygame.K_d] or keys[pygame.K_a]) and \
                not (keys[pygame.K_d] and keys[pygame.K_a]):
            if self.image2Count < 10:
                player.setCurrentImage(3)# = pygame.image.load("CarverSprite/CarverRun0.gif").convert()
                self.image2Count = self.image2Count + 1
            elif self.image2Count < 19:
                player.setCurrentImage(4)# = pygame.image.load("CarverSprite/CarverRun1.gif").convert()
                self.image2Count = self.image2Count + 1
            else:
                self.image2Count = 0
        else:
            player.setCurrentImage(0)# = pygame.image.load("CarverSprite/CarverStill.gif").convert()

        if keys[pygame.K_d]:
            player.setFace("right")
        elif keys[pygame.K_a]:
            player.setFace("left")

        if player.getFace() == "left":
            player.setCurrentImage(pygame.transform.flip(player.getCurrentImage(), 1, 0))


    def __initializePlayerHealth(self):
        return


    """
        Checks for a Victory
    """
    def ifWin(self):
        if self.whoWins != 0:
            return self.whoWins

    """
        Get the keys pressed
    """
    def getKeys(self):
        return self.keys

    """
        Get the local player's Pyfighter
    """
    def getPlayer(self):
        return self.player

    """
        Get the opponent's Pyfighter
    """
    def getOpponent(self):
        return self.opponent

    """
        Set the center of the opponent's shot
    """
    def setShotRect(self, center):
        self.p2ShotRect.center = center

    """
        Get the rectangle for the player's shot
    """
    def getShotRect(self):
        return self.p1ShotRect