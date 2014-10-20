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
        self.currentImage = pygame.image.load("CarverSprite/CarverStill.gif").convert()
        # Pyfighter hit box and character facing
        if player == 1:
            self.hitBox = self.currentImage.get_rect(bottom=585, left=100)
            self.face = "right"
        elif player == 2:
            self.hitBox = self.currentImage.get_rect(bottom=585, left=700)
            self.face = "left"
        # Pyfighter HP
        self.hp = 100

    """
        Set up the image array for the Pyfighter
    """
    def loadImageList(self):

        # Still image of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" + self.name + "Still.gif").convert())
        # Jump image of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" + self.name + "Jump.gif").convert())
        # Melee image of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" + self.name + "Melee.gif").convert())
        # First run frame of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" + self.name + "Run0.gif").convert())
        # Second run frame of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" + self.name + "Run1.gif").convert())
        # Third run frame of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" + self.name + "Run2.gif").convert())
        # Fourth run frame of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" + self.name + "Run3.gif").convert())
        # Shoot image of Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" + self.name + "Shoot.gif").convert())
        # Bullet image for Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" + self.name + "Shot.gif").convert())
        # Bullet contact image for Pyfighter
        self.images.append(pygame.image.load(self.name + "Sprite/" + self.name + "ShotContact.gif").convert())

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
        Set the current image of the Pyfighter
    """
    def setCurrentImage(self, num):
        self.currentImage = self.images[num]

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