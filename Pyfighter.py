__author__ = 'Will Stiles'
import pygame


class Pyfighter:

    """
        Creates a Pyfighter object
    """
    def __init__(self, player, name):
        # Pyfighter speed
        self.speed = [0, 0]
        # Pyfighter name
        self.name = name
        # Pyfighter images
        self.images = []
        self.loadImageList()
        # Current image
        self.currentImage = pygame.image.load(self.name + "Sprite/" + self.name + "Still.gif").convert()
        # Pyfighter hit box and character facing
        if player == 1:
            self.hitBox = self.currentImage.get_rect(bottom=585, left=100)
            self.face = "right"
        elif player == 2:
            # Flip the image for the second player
            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
            self.hitBox = self.currentImage.get_rect(bottom=585, left=700)
            self.face = "left"
        # Pyfighter HP
        self.hp = 100

    """
        Set up the image array for the Pyfighter
    """
    def loadImageList(self):

        # 0 Still image of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" +
                           self.name + "Still.gif").convert())
        # 1 Jump image of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" +
                           self.name + "Jump.gif").convert())
        # 2 Melee image of Pyfighter
        self.images.append(pygame.image.load("OrcSprite/SpitSustain.gif").convert())# self.name + "Sprite/" + self.name + "Melee.gif").convert())
        # 3 First run frame of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" +
                           self.name + "Run0.gif").convert())
        # 4 Second run frame of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" +
                           self.name + "Run1.gif").convert())
        # 5 Third run frame of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" +
                           self.name + "Run2.gif").convert())
        # 6 Fourth run frame of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" +
                           self.name + "Run3.gif").convert())
        # 7 Shoot image of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" +
                           self.name + "Shoot.gif").convert())
        # 8 Bullet image for Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" +
                           self.name + "Shot.gif").convert())
        # 9 Bullet contact image for Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" +
                           self.name + "ShotContact.gif").convert())

    """
        Get the speed of the Pyfighter
    """
    def getSpeed(self):
        return self.speed

    """
        Get the name of the Pyfighter
    """
    def getName(self):
        return self.name

    """
        Get the current image of the Pyfighter
    """
    def getCurrentImage(self):
        return self.currentImage

    """
        Get the hit box of the Pyfighter
    """
    def getHitBox(self):
        return self.hitBox

    """
        Get the facing of the Pyfighter
    """
    def getFace(self):
        return self.face

    """
        Get the hp of the Pyfighter
    """
    def getHP(self):
        return self.hp

    """
        Change the amount of hp for the Pyfighter
    """
    def setHP(self, amount):
        self.hp = amount

    """
        Move the hit box
    """
    def setHitBox(self, center):
        self.hitBox.center = center
        #self.hitBox.centerx = x
        #self.hitBox.centery = y

    """
        Set the face of the Pyfighter
    """
    def setFace(self, face):
        self.face = face

    """
        Set the current image of the Pyfighter
    """
    def setCurrentImage(self, num):
        if type(num) is int:
            self.currentImage = self.images[num]
        else:
            self.currentImage = num

    """
        Set the speed of the Pyfighter on the x axis
    """
    def setPyfighterX(self, num):
        self.speed[0] = num

    """
        Set the speed of the Pyfighter on the y axis
    """
    def setPyfighterY(self, num):
        self.speed[1] = num
