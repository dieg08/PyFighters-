import pygame
import Pyfighter

"""
    A class objectifying a floating platform that a Pyfighter may stand on

    @author     Will Stiles
    @version    October 17, 2014
"""


class Platform:
    """
        Create a platform

        @:param     string      The source of the image
        @:param     centerx     The x coordinate of the center of the platform
        @:param     centery     The y coordinate of the center of the platform
    """
    def __init__(self, string, centerx, centery):
        # Set the image for the platform
        self.plat = pygame.image.load(string).convert()
        # Set a hit box around the platform
        self.platRect = self.longPlat.get_rect(center=(centerx, centery))


    """
        Get the platform image
    """
    def getPlat(self):
        return self.plat

    """
        Get the hit box for the platform
    """
    def getRect(self):
        return self.platRect

    """
        Check if a given Pyfighter is standing on the platform
    """
    def checkStanding(self, fighter):
        # If the Pyfighter is on the platform
        onplat = False
        box = fighter.getHitBox()
        speed = fighter.getSpeed()
        # Hit box checks
        if box.bottom + speed[1] > self.platRect.top and \
           box.left < self.platRect.right and \
           box.right > self.platRect.left and \
           box.top + box.height < self.platRect.top:
            onplat = True
        return onplat
